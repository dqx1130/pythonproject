table = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789+/'

def inttobin(a, n):
    res = bin(a)[2:]
    while len(res) < n:
        res = '0' + res
    return res

def b64encode(strin):
    res = ''
    quotient = len(strin)/3
    remainder = len(strin)%3
    for i in range(quotient):
        tmp = strin[i*3:i*3+3]
        tmpbin = inttobin(ord(tmp[0]), 8) + inttobin(ord(tmp[1]), 8) + inttobin(ord(tmp[2]), 8)
        print(tmpbin)
        for j in range(4):
            index = int(tmpbin[6*j:6*j+6], 2)
            res += table[index]
    if remainder == 1:
        tmpbin = inttobin(ord(strin[-1]), 8) + '0000'
        res += table[int(tmpbin[:6], 2)]
        res += table[int(tmpbin[6:], 2)]
        res += '=='
    elif remainder == 2:
        tmpbin = inttobin(ord(strin[-2]), 8) + inttobin(ord(strin[-1]), 8) + '00'
        res += table[int(tmpbin[:6], 2)]
        res += table[int(tmpbin[6:12], 2)]
        res += table[int(tmpbin[12:], 2)]
        res += '='
    return res

def b64decode(strin):
    res = ''
    while strin[-1] == '=':
        strin = strin[:-1]
    tmpbin = ''
    for i in range(len(strin)):
        tmpbin += inttobin(table.index(strin[i]), 6)
    remainder = len(tmpbin) / 8
    for i in range(remainder):
        res += chr(int(tmpbin[i*8:i*8+8], 2))
    return res