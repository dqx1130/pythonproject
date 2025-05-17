power = {"吕布": 999, "关羽": 888, "刘备": 666, "张飞": 900, "赵云": 789, "不二如是": 999}
# 请 lambda 表达式和 filter() 函数配合，替换下面的代码
# greater = []
# for k, v in power.items():
#     if v > 800:
#         greater.append((k, v))
# print(greater)
# [('吕布', 999), ('关羽', 888), ('张飞', 900), ('不二如是', 999)]
greater  = list(filter(lambda x : x[1] > 800 , power.items()))
print(greater)
