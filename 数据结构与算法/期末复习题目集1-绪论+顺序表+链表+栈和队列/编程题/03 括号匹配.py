import queue
def cop(s):
    dict1 = {"}":"{","]":"[",")":"("}
    Q = queue.LifoQueue()
    for each in s:
        if each in dict1.values():
            Q.put(each)
        if each in dict1.keys():
            if Q.empty():
                return False
            if dict1[each] != Q.get():
                return False
    return Q.empty()

s = input()
cop(s)

