class Solution(object):
    def findLUSlength(self, a, b):
        """
        :type a: str
        :type b: str
        :rtype: int
        """
        if len(a) == len(b):
            if a != b:
                return len(a)
            else:
                return -1
        lenMax = -1
        i1 = 0
        i2 = 0
        #循环检测
        while i1 <= len(a) :
            for j1 in range(i1,len(a)+1):
                tmp = a[i1:j1]
                #判是否撞车对面子序列
                if tmp not in b and len(a[i1:j1]) > lenMax :
                    lenMax = len(a[i1:j1])
            i1 += 1
        while i2 <= len(b) :
            for j2 in range(i2,len(b)+1):
                tmp = b[i2:j2]
                #判是否撞车对面子序列
                if tmp not in a and len(b[i2:j2]) > lenMax:
                    lenMax = len(b[i2:j2])
            i2 += 1
        return lenMax

S = Solution()
print(S.findLUSlength("aefawfawfawfaw","aefawfeawfwafwaef"))
