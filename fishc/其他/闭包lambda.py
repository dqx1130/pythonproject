# def maker(n):
#     def action(x):
#         return x ** n
#     return action
# x = int(input())
# n = 2
# f = maker(x)
# print(f(n))

maker = lambda n : lambda x: x ** n
x = int(input())
n = 2
f = maker(n)
print(f(x))