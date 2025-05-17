class Node:
    def __init__(self, char='', freq=0.0):
        self.char = char      # 字符
        self.freq = freq      # 频率
        self.left = None      # 左子节点
        self.right = None     # 右子节点
        self.code = ''        # 编码

def create_huffman_tree(chars, freqs):
    # 创建初始节点列表
    nodes = [Node(chars[i], freqs[i]) for i in range(len(chars))]
    
    while len(nodes) > 1:
        # 按频率排序，频率相同时按输入顺序排序（通过列表索引保持）
        nodes.sort(key=lambda x: x.freq)
        
        # 取出频率最小的两个节点
        left = nodes.pop(0)
        right = nodes.pop(0)
        
        # 创建新的内部节点
        internal = Node()
        internal.freq = left.freq + right.freq
        internal.left = left
        internal.right = right
        
        # 将新节点加入列表
        nodes.append(internal)
    
    return nodes[0] if nodes else None

def generate_codes(root, code=''):
    if root is None:
        return {}
    
    # 如果是叶子节点，记录编码
    if root.char:
        return {root.char: code}
    
    # 递归生成左右子树的编码
    codes = {}
    codes.update(generate_codes(root.left, code + '0'))
    codes.update(generate_codes(root.right, code + '1'))
    return codes

def main():
    # 读取测试用例数量
    T = int(input())
    
    for _ in range(T):
        # 读取字符数量
        n = int(input())
        
        # 读取字符和频率
        chars = []
        freqs = []
        for _ in range(n):
            char, freq = input().split()
            chars.append(char)
            freqs.append(float(freq))
        
        # 创建哈夫曼树
        root = create_huffman_tree(chars, freqs)
        
        # 生成编码
        codes = generate_codes(root)
        
        # 按输入顺序输出编码
        result = []
        for char in chars:
            result.append(f"{char}: {codes[char]}")
        
        print(" ".join(result))

if __name__ == "__main__":
    main()