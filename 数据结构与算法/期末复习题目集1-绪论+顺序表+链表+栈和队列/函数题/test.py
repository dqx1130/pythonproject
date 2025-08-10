import queue
def check(s):
    Q = queue.LifoQueue()
    dic = {"}":"{","]":"[",")":"("}
    for each in s:
        if each in "}])":
            if Q.empty():
                return False
            if Q.get() != dic[each]:
                return False

        if each in "{[(":
            Q.put(each)

    if not Q.empty:
        return False
    return True



s = input()
print(check(s))


