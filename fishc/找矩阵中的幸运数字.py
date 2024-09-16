list = [[10, 36, 52],
        [33, 24, 88],
        [66, 76, 99]]

rows = len(list)
columns = len(list[0])
print("读取行数：",rows,"行")
print("读取列数：",columns,"列")
print("")

minrows = [1024] * rows
maxcolumns = [0] * columns
print("minrows为",minrows)
print("maxcolumns为",maxcolumns)
print("")

for a in range(rows):
    for b in range(columns):
        minrows[a] = min(list[a][b], minrows[a])
        maxcolumns[b] = max(list[a][b], maxcolumns[b])
print("现在minrows为",minrows)
print("现在maxcolumns为",maxcolumns)
print("")

for a in range(rows):
    for b in range(columns):
        if list[a][b] == minrows[a] and list[a][b] == maxcolumns[b]:
            print("结果为",list[a][b])


# matrix = [[10, 36, 52],
#           [33, 24, 88],
#           [66, 76, 99]]
#
# row = len(matrix)
# col = len(matrix[0])
# print("读取行数：",row,"行")
# print("读取列数：",col,"列")
# print("")
#
# min_row = [1024] * row
# max_col = [0] * col
# print("min_row为",min_row)
# print("max_col为",max_col)
# print("")
#
# # 遍历矩阵中的每一个元素
# # 找到每行中最小的元素，并将它们存放到列表min_row中
# # 找到每列中最大的元素，并将它们存放到列表max_col中
# for i in range(row):
#     for j in range(col):
#         min_row[i] = min(matrix[i][j], min_row[i])
#         max_col[j] = max(matrix[i][j], max_col[j])
#
# print("现在min_row为",min_row)
# print("现在max_col为",max_col)
# print("")
#
# # 遍历矩阵中的每一个元素
# # 判断是否同时满足“同一行的所有元素中最小”和“同一列的所有元素中最大”
# for i in range(row):
#     for j in range(col):
#         if matrix[i][j] == min_row[i] and matrix[i][j] == max_col[j]:
#             print("结果为",matrix[i][j])