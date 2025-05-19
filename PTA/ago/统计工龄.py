people  = int(input())
age = sorted(map(int,input().split()))
data = {}.fromkeys(age,0)
# print(age)
# print(data)
for each in age:
    if each in data:
        data[each]+=1
# print(data)
for key,value in data.items():
    print(f"{key}:{value}")