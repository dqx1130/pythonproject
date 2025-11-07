import base64


def decode(s):
    n = 1
    while True:
        try:
            s = base64.b64decode(s)
            n += 1
        except:
            print('Base64共decode了{0}次，最终结果如下：'.format(n))
            print(str(s, 'utf-8'))
            break


if __name__ == "__main__":
    f = open("C:/Users/mimo/Desktop/flag.txt", 'r').read()
    decode(f)
#注意更改路径
#末尾没有==使用这个
