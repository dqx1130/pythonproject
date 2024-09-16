import re

def read_file(filepath):
    with open(filepath) as fp:
        content = fp.read();
    return content

number = read_file(r'C:\Users\Administrator\Desktop\thienc.txt')
result = []
result.append(re.findall(r'.{2}', number))
result = result[0]

strings = ''
for i in result:
    y = bytearray.fromhex(i)
    z = str(y)
    z = re.findall("b'(.*?)'", z)[0]
    strings += z

b = strings.split('0x')

strings = ''
for i in b:
    if len(i) == 1:
        i = '0' + i
    strings += i

with open(r'C:\Users\Administrator\Desktop\flag.txt', 'w') as f:
    f.write(strings)
    f.close()