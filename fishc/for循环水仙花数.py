import math
count = 0
for a in range(100,1000,1):
    num_1 = str(a)[0]
    num_2 = str(a)[1]
    num_3 = str(a)[2]
    if a == math.pow(int(num_1),3) + math.pow(int(num_2),3) + math.pow(int(num_3),3):
    #math.pow(底数,幂)   例如，math.pow(2,3)就是2的3次方
        print(a)