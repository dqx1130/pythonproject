list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 8, 8, 5, 6, 3, 2, 1, 2]
list_copy = list
list_copy.reverse()
print(list_copy) #代码写一半的测试
lenth = len(list)
location = lenth - 1 - list_copy[list_copy.index(1)] #减 1 是因为 list下标从0开始，数数从1开始，相差一位数。
print(location)