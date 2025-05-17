total = int(input()) + 1
time = []
for _ in range(total):
    tmp = input()
    if tmp == "0":
        break
    a , b = map(int,tmp.split())
    tmp = [a,b]
    time.append(tmp)
time = sorted(time,key= lambda x:x[1] , reverse= False)
# print(time)
end = time[0][1]
res = 1
for each in time:
    if each[0] >= end:
        end = each[1]
        res += 1
print(res)