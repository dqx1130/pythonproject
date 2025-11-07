#Huffman Encoding
#Tree-Node Type

import random
class Node:
    def __init__(self,freq):
        self.left = None
        self.right = None
        self.father = None
        self.freq = freq
    def isLeft(self):
        return self.father.left == self
#create nodes创建叶子节点
def createNodes(freqs):
    return [Node(freq) for freq in freqs]

#create Huffman-Tree创建Huffman树
def createHuffmanTree(nodes):
    queue = nodes[:]
    print(queue) #一个个node的地址
    #每次对queue进行排序，
    while len(queue) > 1:
        queue.sort(key=lambda item:item.freq) #reverse = false
        node_left = queue.pop(0)
        node_right = queue.pop(0)
        node_father = Node(node_left.freq + node_right.freq)
        node_father.left = node_left
        node_father.right = node_right
        node_left.father = node_father
        node_right.father = node_father
        queue.append(node_father)
    queue[0].father = None
    return queue[0]
#Huffman编码
def huffmanEncoding(nodes,root):
    codes = [''] * len(nodes)
    for i in range(len(nodes)):
        node_tmp = nodes[i]
        while node_tmp != root:
            if node_tmp.isLeft():
                codes[i] = '0' + codes[i]
            else:
                codes[i] = '1' + codes[i]
            node_tmp = node_tmp.father
    return codes

def freq_count(strr):
    chars = []
    chars_fre = []
    for i in range(len(strr)):
        if strr[i] in chars:
            pass
        else:
            chars.append(strr[i])
            char_fre = (strr[i], strr.count(strr[i]))
            chars_fre.append(char_fre)
    return chars_fre

def encoder_huffman(strr,chars_fre,codes):
    huffmans=''
    for word in strr:
        i = 0
        #用于与code【i】还有item 的符号一一对应
        for item in chars_fre:
            if word == item[0]:
                huffmans += codes[i]
            i += 1
    print(huffmans)
    return huffmans

def decode_huffman(huffmans,codes,chars_fre):
    original_code=''
    while huffmans!='':
        i=0
        for item in codes:
            if item in huffmans:
                if huffmans.index(item) ==0:
                    original_code += chars_fre[i][0]
                    huffmans=huffmans[len(item):]
            i+=1
    return original_code

if __name__ =='__main__':
    sttttt=""
    sttttt = open('docx.txt','r').read()#docx.txt为Oliver Twist.docx中提取出来的文字
    chars_freqs =[]
    chars_freqs = freq_count(sttttt)
    print('文本中字符的统计如下：\n'+str(chars_freqs))
    nodes = createNodes([item[1] for item in chars_freqs])
    root = createHuffmanTree(nodes)
    codes = huffmanEncoding(nodes,root)
    res = {}
    for item in zip(chars_freqs,codes):
        print ('Character:%s freq:%-2d   encoding: %s' % (item[0][0],item[0][1],item[1]))
        res.update({item[1]:item[0][0]})
    print(res)
    d2 = open('flag.txt','r').readlines()#flag.txt为outguess提取出来的编码
    re = ''
    for i in d2:
        re+=res[i[:-1]]
    print(re)
