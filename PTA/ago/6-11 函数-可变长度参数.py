def WordCount(*word):
    # 将所有单词转为小写，并统计每个单词的出现次数
    word_count = {}
    for w in word:

        w = w.lower()  # 转换为小写
        if w in word_count:
            word_count[w] += 1
        else:
            word_count[w] = 1
        # print(word_count)
    # 将字典按频率降序排序，若频率相同则按字母顺序升序排序
    sorted_word_count = sorted(word_count.items(), key=lambda x: (-x[1], x[0]))
    return sorted_word_count
listword = "They were from the Middle West from the Far West from Old World England".split()
sortword = WordCount(*listword)
print(list(sortword))
# print(sortword)