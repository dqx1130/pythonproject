# 用一个人类来描述如何使用类的属性
class Person:                        #定义一个人类
    role = 'person'                  #角色属性都是人
    def __int__(self,name):
        self.name = name             #每一个角色都有自己的昵称
    def walk(self):                  #人都可以走路,也就是有一个走路方法
        print("person is walking……")

print(Person.role)                   #查看人的role属性
print(Person.walk)                   #引用人的walk方法,注意，这里不是在调用

#self在实例化时自动将对象／实例本身传给__init__的第一个参数，也可以给它起个别的名字，但是一般都不会这么做。