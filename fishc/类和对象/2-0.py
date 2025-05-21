class A:
    x = 250
class B:
    x = 520

class C(B):
    pass
class D(A,B):
    pass
class E():
    pass
class F(D):
    pass
class G(D):
    pass
class H(E,F,G):
    pass

h = H
print(h.x)
