s = '001100010011001000110011001101000011010100110110001101110011100000'
def bin2asc(string):
    temp = ''
    for i in range(int(len(string) / 8)):
        temp += chr(int(string[i * 8: i * 8 + 8], 2))
    print(temp)
    return
bin2asc(s)
