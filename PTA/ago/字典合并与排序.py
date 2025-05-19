a = dict(eval(input()))
b = dict(eval(input()))
# a = dict(eval("{1:2,3:9,5:2,6:2}"))
# b = dict(eval("{2:1,6:3,7:9,1:4}"))
for k in b.keys():
    a[k] = a.get(k,0) + b[k]
a = sorted(a.items(), key=lambda x:x[0], reverse=False)
print(dict(a))