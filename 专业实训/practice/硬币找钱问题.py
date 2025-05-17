def getCoins(price,coinMax):
    coinList = [200, 100, 50, 20, 10, 5]
    total = 0
    for i in range(len(coinMax)):
        count = price // coinMax[i]
        if count > coinMax[i]:
            count = coinMax[i]
        total += count
        price -= coinList[i] * count 
        if price == 0:
            break
    if price > 0:
        return "No"
    return total 



times = int(input())
tmp = list(map(float,input().split()))
coinMax = tmp[0:6]
price = tmp[-1] * 100
print(coinMax)
price = int(price + 0.5)
print(price)
coinMax = coinMax[::-1]
print(coinMax)
