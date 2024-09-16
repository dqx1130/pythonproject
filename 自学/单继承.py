#类定义
class people:
    name = ''
    sex = 0
    __height = 0
    def __int__(self, n, a, w):
        self.name = n
        self.sex = a
        self.__height = w
    def speak(self):
        print("%s说：我的性别是%s。"%(self.name,self.sex))
#单继承实例
class son(people):
    grade = ''
    def __init__(self, n, a, w, g):
        #调用父类的构造函数
        people.__init__(self, n, a, w)
        self.grade = g
    #覆写父类的方法
    def speak(self):
        print("%s说：我的性别是%s，我在读%s年级"%(self.name,self.sex,self.grade))
s = son('小明','男',12,6)
s.speak()
