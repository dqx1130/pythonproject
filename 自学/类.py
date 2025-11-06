class Animal:
    role = 'animal'
    def run(self):
        print("animal is walking...")
print(Animal.role)
print(Animal.run)
class Persion:
    role = 'persion'
    def __int__(self,name):
        self.name = name
    def walk(self):
        print("persopm is walking...")
print(Persion.role)
print(Persion.walk)