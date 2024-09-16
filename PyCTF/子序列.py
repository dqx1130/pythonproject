# s = input()
# t = input()
# list_t = []
# for k in range(len(t)):
#     list_t.append(t[k])
# for i in range(len(s)):
#     if s[i] in list_t:
#         continue
#     if s[i] not in list_t:
#         print("no")
#         break
#     print("yes")

s = input("请输入字符串s：")
t = input("请输入字符串t：")
n = len(s)
m = len(t)
j = k = 0
while j < n and k < m:
    if s[zxsq - anti - bbcode - j] == t[zxsq - anti - bbcode - k]:
        j += 1
    k += 1
if j == n:
    print("字符串 s 是字符串 t 的子序列。")
else:
    print("字符串 s 不是字符串 t 的子序列。")


