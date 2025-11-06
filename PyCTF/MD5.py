import hashlib
def get_md5(s):
    """获取MD5加密值

    :param s: 需要加密的字符串
    :return: 密文
    """
    if s:
        m = hashlib.md5()
        if s is str:
            m.update(s.encode("UTF-8"))
        else:
            m.update(str(s).encode("UTF-8"))
        return m.hexdigest()
    raise ValueError("传入参数不能为空")
str = '8f9bd0a7-7884-4271-aba6-9dd6ead45fd43bf9f6cf685a6dd8defadabfb41a03a1'

str_md5 = get_md5(str)

print(str_md5)