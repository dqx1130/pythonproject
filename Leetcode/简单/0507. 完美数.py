class Solution:
    def checkPerfectNumber(self, num: int) -> bool:
        #特判
        if num == 1:
            return False
        # 找正因子
        listY = [1]
        for i in range(2,int(pow(num,0.5)) + 1):
            #过滤有的，节省时间
            if i in listY:
                continue
            #找因子(整除)
            if num % i == 0:
                listY.append(i)
                listY.append(num//i)
        if sum(listY) == num:
            return True
        else:
            return False
