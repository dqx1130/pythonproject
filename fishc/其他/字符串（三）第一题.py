#给定一个字符串 text 和字符串列表 words，
#返回 words 中每个单词在 text 中的位置，
#要求最终的位置从小到大进行排序。
text = input("请输入text的内容：")          
words = input("请输入words的内容：")
words = words.split()      #将每一个单词都存放进word列表中，此时的word从字符串变成了列表

result = []
for each in words:
    temp = text.find(each)
    while temp != -1:
        result.append([temp,temp+len(each)-1])
        temp = text.find(each, temp+1)
    
print(sorted(result))