
s = [2 ,2 ,2 ,2 ,1 ,2,2 ,2 ,2]
left = 0
right = len(s)
print(right - left)
mid = (left+right)//2
print(mid)
print(s[left:mid])
print(s[mid+1:right])