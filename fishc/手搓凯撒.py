plain = list(input("请输入需要加密的明文（只支持英文字母）："))

key = int(input("请输入移动的位数："))

base_A = ord("A")

base_a = ord("a")

cipher = []

for each in plain:
    if each == " ":
        cipher.append(each)
    else:
        if each.isupper():
            base = base_A
        else:
            base = base_a
        cipher.append(chr((ord(each) - base + key) % 26 + base))
        # ascii偏移防止溢出
    result = "".join(cipher)
print(result)
