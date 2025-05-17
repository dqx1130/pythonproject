class Rational:
    def __init__(self, a, b):
        self.a = a
        self.b = b
        self.__simple__()
    
    def __gcd__(self, a, b):
        while b:
            a, b = b, a % b
        return a
        
    def __simple__(self):
        g = self.__gcd__(self.a, self.b)
        self.a = self.a // g
        self.b = self.b // g
    
    def getFz(self):
        return self.a

    def getFm(self):
        return self.b
    
    def __add__(self, x):
        new_a = self.a * x.b + x.a * self.b
        new_b = self.b * x.b
        return Rational(new_a, new_b)
    
    def __sub__(self, x):
        new_a = self.a * x.b - x.a * self.b
        new_b = self.b * x.b
        return Rational(new_a, new_b)
    
    def __mul__(self, x):
        new_a = self.a * x.a
        new_b = self.b * x.b
        return Rational(new_a, new_b)
    
    def __str__(self):
        return f"{self.a}/{self.b}"