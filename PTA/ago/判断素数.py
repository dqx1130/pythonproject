def isPrime(n):
    if n == 1 or n == 0:
        return False
    else:
        for i in range(2,int(pow(n,0.5))+1):
            if n % i == 0:
                return False
        return True

num = int(input())        #接收用户输入并转成整数
for i in range(num+1):
    if isPrime(i):
        print(i,end=' ')  #在同一行内输出结果，不换行，中间用空格分隔