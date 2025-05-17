import xpinyin
def huiwen(text):
    result = xpinyin.Pinyin().get_pinyin(text)
    list1 = result.split("-")
    list2 = list(reversed(list1))
    if list1 == list2:
        print(f"[{text}]是回文。")
    elif list1 !=list2:
        print(f"[{text}]不是回文。")
    return text
while True:
    text = input("请输入一段话:")
    while len(text) < 3:
        text = input("字数太少，请输入一段话:")
    huiwen(text)
    break

