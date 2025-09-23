# -*- encoding: utf-8 -*-
'''
@File    :   app.py
@Time    :   2066/07/05 19:20:29
@Author  :   Ekko exec inc. 某牛马程序员
'''

import os
import time
import uuid
import requests

from functools import wraps
from datetime import datetime
from secrets import token_urlsafe
from flask_sqlalchemy import SQLAlchemy
from werkzeug.security import generate_password_hash, check_password_hash
from flask import Flask, render_template, redirect, url_for, request, flash, session

# 服务器启动时间，用于记录服务器何时启动
SERVER_START_TIME = time.time()

# 下面两行仅为调试，实际未用到random库，留作纪念
import random
random.seed(SERVER_START_TIME)  # 用服务器启动时间初始化随机种子

# 生成一个超级管理员初始密码，每次启动随机生成
admin_super_strong_password = token_urlsafe()

# Flask应用实例化
app = Flask(__name__)
# Flask配置项
app.config['SECRET_KEY'] = 'your-secret-key-here'  # 用于Session加密
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///site.db'  # SQLite数据库文件路径
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False  # 关闭SQLAlchemy的事件系统提高性能

# SQLAlchemy数据库对象
db = SQLAlchemy(app)

# ---------------------- 数据模型定义 ----------------------

class User(db.Model):
    """
    用户表模型
    id: 主键
    username: 用户名，唯一且不能为空
    email: 邮箱，唯一且不能为空
    password: 密码哈希值
    is_admin: 是否为管理员
    time_api: 用户自定义的时间API地址
    """
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(20), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password = db.Column(db.String(60), nullable=False)
    is_admin = db.Column(db.Boolean, default=False)
    time_api = db.Column(db.String(200), default='https://api.uuni.cn//api/time')


class PasswordResetToken(db.Model):
    """
    密码重置Token表
    id: 主键
    user_id: 外键关联User
    token: 重置用的唯一Token
    used: 是否已被使用
    """
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    token = db.Column(db.String(36), unique=True, nullable=False)
    used = db.Column(db.Boolean, default=False)

# ---------------------- 辅助函数 ----------------------

def padding(input_string):
    """
    将字符串转成长度为6字节，不足补0，超出截断，并转为整数（大端字节序）
    用于自定义uuid参数
    """
    byte_string = input_string.encode('utf-8')
    if len(byte_string) > 6:
        byte_string = byte_string[:6]
    padded_byte_string = byte_string.ljust(6, b'\x00')
    padded_int = int.from_bytes(padded_byte_string, byteorder='big')
    return padded_int

# ---------------------- 数据库初始化及管理员创建 ----------------------

with app.app_context():
    db.create_all()  # 创建所有表
    # 如果没有管理员账户，则默认创建一个admin
    if not User.query.filter_by(username='admin').first():
        admin = User(
            username='admin',
            email='admin@example.com',
            password=generate_password_hash(admin_super_strong_password),
            is_admin=True
        )
        db.session.add(admin)
        db.session.commit()

# ---------------------- 登录/权限装饰器 ----------------------

def login_required(f):
    """
    检查用户是否已登录，未登录则重定向到登录页
    """
    @wraps(f)
    def decorated_function(*args, **kwargs):
        if 'user_id' not in session:
            flash('请登录', 'danger')
            return redirect(url_for('login'))
        return f(*args, **kwargs)
    return decorated_function

def admin_required(f):
    """
    检查用户是否为管理员，未登录或非管理员则重定向
    """
    @wraps(f)
    def decorated_function(*args, **kwargs):
        if 'user_id' not in session:
            flash('请登录', 'danger')
            return redirect(url_for('login'))
        user = User.query.get(session['user_id'])
        if not user.is_admin:
            flash('你不是admin', 'danger')
            return redirect(url_for('home'))
        return f(*args, **kwargs)
    return decorated_function

# ---------------------- 检查时间API ----------------------

def check_time_api():
    """
    调用用户自定义的时间API，解析返回的date字段，
    并判断年份是否大于等于2066
    """
    user = User.query.get(session['user_id'])
    try:
        response = requests.get(user.time_api)
        data = response.json()
        datetime_str = data.get('date')
        if datetime_str:
            print(datetime_str)
            current_time = datetime.fromisoformat(datetime_str)
            return current_time.year >= 2066
    except Exception as e:
        return None
    return None

# ---------------------- 路由视图函数 ----------------------

@app.route('/')
def home():
    """
    首页
    """
    return render_template('home.html')

@app.route('/server_info')
@login_required
def server_info():
    """
    显示服务器的启动时间和当前时间，仅登录后可见
    """
    return {
        'server_start_time': SERVER_START_TIME,
        'current_time': time.time()
    }

@app.route('/register', methods=['GET', 'POST'])
def register():
    """
    注册页面及逻辑
    - 检查两次密码是否一致
    - 用户名和邮箱唯一性检查
    - 注册成功后跳转到登录页
    """
    if request.method == 'POST':
        username = request.form.get('username')
        email = request.form.get('email')
        password = request.form.get('password')
        confirm_password = request.form.get('confirm_password')

        if password != confirm_password:
            flash('密码错误', 'danger')
            return redirect(url_for('register'))

        existing_user = User.query.filter_by(username=username).first()
        if existing_user:
            flash('已经存在这个用户了', 'danger')
            return redirect(url_for('register'))

        existing_email = User.query.filter_by(email=email).first()
        if existing_email:
            flash('这个邮箱已经被注册了', 'danger')
            return redirect(url_for('register'))

        hashed_password = generate_password_hash(password)
        new_user = User(username=username, email=email, password=hashed_password)
        db.session.add(new_user)
        db.session.commit()

        flash('注册成功，请登录', 'success')
        return redirect(url_for('login'))

    return render_template('register.html')

@app.route('/login', methods=['GET', 'POST'])
def login():
    """
    登录页面及逻辑
    - 检查用户名和密码
    - 登录成功后保存用户信息到session
    """
    if request.method == 'POST':
        username = request.form.get('username')
        password = request.form.get('password')

        user = User.query.filter_by(username=username).first()
        if user and check_password_hash(user.password, password):
            session['user_id'] = user.id
            session['username'] = user.username
            session['is_admin'] = user.is_admin
            flash('登陆成功，欢迎!', 'success')
            return redirect(url_for('dashboard'))
        else:
            flash('用户名或密码错误!', 'danger')
            return redirect(url_for('login'))

    return render_template('login.html')

@app.route('/logout')
@login_required
def logout():
    """
    登出，清除session
    """
    session.clear()
    flash('成功登出', 'info')
    return redirect(url_for('home'))

@app.route('/dashboard')
@login_required
def dashboard():
    """
    用户登录后的主面板
    """
    return render_template('dashboard.html')

@app.route('/forgot_password', methods=['GET', 'POST'])
def forgot_password():
    """
    忘记密码页面及逻辑
    - 通过邮箱查找用户
    - 生成密码重置Token并保存
    - TODO: 发送邮件（目前未实现）
    """
    if request.method == 'POST':
        email = request.form.get('email')
        user = User.query.filter_by(email=email).first()
        if user:
            # 生成自定义UUID（v8），用用户名做参数
            token = str(uuid.uuid8(a=padding(user.username)))
            reset_token = PasswordResetToken(user_id=user.id, token=token)
            db.session.add(reset_token)
            db.session.commit()
            # TODO：写一个SMTP服务把token发出去
            flash(f'密码恢复token已经发送，请检查你的邮箱', 'info')
            return redirect(url_for('reset_password'))
        else:
            flash('没有找到该邮箱对应的注册账户', 'danger')
            return redirect(url_for('forgot_password'))

    return render_template('forgot_password.html')

@app.route('/reset_password', methods=['GET', 'POST'])
def reset_password():
    """
    重置密码页面及逻辑
    - 检查token有效性
    - 修改用户密码并标记token已用
    """
    if request.method == 'POST':
        token = request.form.get('token')
        new_password = request.form.get('new_password')
        confirm_password = request.form.get('confirm_password')

        if new_password != confirm_password:
            flash('密码不匹配', 'danger')
            return redirect(url_for('reset_password'))

        reset_token = PasswordResetToken.query.filter_by(token=token, used=False).first()
        if reset_token:
            user = User.query.get(reset_token.user_id)
            user.password = generate_password_hash(new_password)
            reset_token.used = True
            db.session.commit()
            flash('成功重置密码！请重新登录', 'success')
            return redirect(url_for('login'))
        else:
            flash('无效或过期的token', 'danger')
            return redirect(url_for('reset_password'))

    return render_template('reset_password.html')

@app.route('/execute_command', methods=['GET', 'POST'])
@login_required
def execute_command():
    """
    执行命令页面
    - 检查时间API（只有2066年后才可用）
    - POST时执行用户输入的命令（极不安全，仅测试用）
    """
    result = check_time_api()
    if result is None:
        flash("API死了啦，都你害的啦。", "danger")
        return redirect(url_for('dashboard'))

    if not result:
        flash('2066年才完工哈，你可以穿越到2066年看看', 'danger')
        return redirect(url_for('dashboard'))

    if request.method == 'POST':
        command = request.form.get('command')
        os.system(command)  # 安全隐患，生产环境千万别用
        return redirect(url_for('execute_command'))

    return render_template('execute_command.html')

@app.route('/admin/settings', methods=['GET', 'POST'])
@admin_required
def admin_settings():
    """
    管理员设置页面
    - 允许管理员更改time_api字段
    """
    user = User.query.get(session['user_id'])

    if request.method == 'POST':
        new_api = request.form.get('time_api')
        user.time_api = new_api
        db.session.commit()
        flash('成功更新API！', 'success')
        return redirect(url_for('admin_settings'))

    return render_template('admin_settings.html', time_api=user.time_api)

# ---------------------- 启动应用 ----------------------

if __name__ == '__main__':
    # 以0.0.0.0监听，允许外部访问；生产环境应关闭debug
    app.run(debug=False, host="0.0.0.0")