import turtle #导入turtle库
turtle.pensize(4)#设置画笔像素为4像素
turtle.pencolor("red")
turtle.fillcolor("red")
turtle.begin_fill()
turtle.left(135)
turtle.forward(100)
turtle.circle(-50,180)#第一个半圆
turtle.left(90)
turtle.circle(-50,180)#第二个半圆
turtle.forward(100)
turtle.end_fill()#结束填充
turtle.done()

