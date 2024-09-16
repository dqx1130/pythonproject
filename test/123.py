first , last = input().split()
first , last = eval(first), eval(last)
n = 0
sum = 0
for i in range(first,last+1):
    print(f"{i:>5}" ,end = '')
    n += 1
    sum = sum + i
    if n % 5 == 0 or i == last :
        print()
print(f"Sum = {sum}")

# a,b=map(int,input().split())
# sum = 0
# count = 0
# for i in range(a,b+1):
#     sum+=i
#     count+=1
#     print(f'{i:5d}',end='')
#     if count%5==0 or i==b:
#         print()
# print(f'Sum = {sum}')
