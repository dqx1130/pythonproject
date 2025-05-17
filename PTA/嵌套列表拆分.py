def chai(text):
    if not isinstance(text, list):
        return [text]
    res = []
    for each in text:
        res.extend(chai(each))
    return res

text = [[1, 2], 3, [4, 5, ['a', 'b']], [[[[['c']]]]]]
# text = eval(input())
print(chai(text))
