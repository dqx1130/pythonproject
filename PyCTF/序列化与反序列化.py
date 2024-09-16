import json

def serialize(dict):
    output = json.dumps(dict,ensure_ascii=False)
    print(output)

def unserialize(dict):
    output = json.loads(dict,ensure_ascii=False)
    print(output)

dict={'姓名':'张三'}
serialize(dict)
