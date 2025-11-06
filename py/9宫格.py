def jiujian(get):
    if not get:
        return []
    keyboard = {
        "2":'abc',
        '3':'def',
        '4':'ghi',
        '5':'jkl',
        '6':'mno',
        '7':'pqrs',
        '8':'tuv',
        '9':'wxyz'
    }
    res = []
    if len(get) == 0:
        return []
    if len(get) == 1:
        return keyboard[get]
    restult = jiujian(get[1:])
    for i in restult:
        for j in keyboard[get[0]]:
            res.append((j+i))
    return res

print(jiujian(input("请输入数字：")))