file = open(r"C:\Users\Administrator\Desktop\123.csv")
ls = []
for line in file:
    line = line.replace("\n","")
    ls.append(line.split(','))
print(ls)
file.close()
