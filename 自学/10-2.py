#创建一个类
class Data:
    pass

#定义函数的属性
class Animal:                          #定义一个动物类
    role = 'animal'                    #角色属性都是动物(类的静态属性)
    def run(self):                     #动物可以跑，也就是有一个跑的方法，也叫动态属性
        print("animal is walking……")
        