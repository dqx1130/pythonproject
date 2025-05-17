import random
def main():
    data = input("请输入需要打乱的序列：")
    times = input("请输入需要打乱的次数：")
    # data = "ABCDEFG"
    # times = "3"
    result = ""
    #打乱功能
    for time in range(int(times)):
        judge = len(data)
        while judge > 0:
            index = random.randint(0,len(data)-1)
            # print("随机索引：",index)
            judge -= 1
            result += data[index]
            data = data[0:index] + data[index+1:] #去除索引指定的字符
            # print("data:",data)
            # print("result:",result)
        print(f"第{time+1}次打乱后的结果：{result}")
        data = result
        result = ""
main()

