x = int(input("请输入x坐标："))
y = int(input("请输入y坐标："))
print("坐标("+str(x)+","+str(y)+")")
# x=1
# y=2
if x > 0 and y > 0:
    print("坐标点位于第一象限")
elif x < 0 and y >0:
    print("坐标点位于第二象限")
elif x < 0 and y > 0:
    print("坐标点位于第三象限")
elif x < 0 and y > 0:
    print("坐标点位于第四象限")
elif x == 0 and y == 0:
    print("坐标点位于坐标原点")
elif x == o and y != 0:
    print("坐标点位于y轴")
else:
    print("坐标点位于x轴")



