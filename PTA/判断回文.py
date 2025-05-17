def huiwen(s):
    if s[::-1] == s:
        return True
    else:
        return False

s=input()
if huiwen(s)==1:print("{}是回文".format(s))
else:print("{}不是回文".format(s))