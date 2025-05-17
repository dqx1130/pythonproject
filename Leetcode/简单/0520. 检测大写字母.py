class Solution:
    def detectCapitalUse(self, word: str) -> bool:
        if len(word) == 1:
            return True
        #首字母大写
        if "A" <= word[0] <= "Z":
            if "A" <= word[1] <= "Z":
                #接下来都要大写
                for i in range(2,len(word)):
                    if  word[i] < "A" or word[i] > "Z":
                        return False

            elif "a" <= word[1] <= "z":
                # 接下来都要小写
                for i in range(2, len(word)):
                    if word[i] < "a" or word[i] > "z":
                        return False
        #首字母小写
        if "a" <= word[0] <= "z":
            # 接下来都要小写
            for i in range(1, len(word)):
                if word[i] < "a" or word[i] > "z":
                    return False
        return True

