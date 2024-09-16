# 用一个动物类来描述如何使用类的属性
# 定义函数的属性
class Animal:               # 定义一个动物类
    role = 'animal'         # 角色属性都是动物(类的静态属性)
    def run(self):          # 动物都可以跑，也就是有一个跑的方法，也叫动态属性
        print("animal is walking……")

print(Animal.role)          # 查看动物的role属性
print(Animal.run)           # 引用动物的run方法,注意,这里不是在调用！！！！！！！！！
