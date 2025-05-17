class Solution(object):
    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        digits = map(str,digits)
        txt = ''.join(digits)
        num = int(txt)
        num += 1
        txt = str(num)
        res = []
        for each in txt:
            res.append(int(each))
        return res