file = open(r"C:\Users\Administrator\Desktop\123.csv","w+",encoding='utf-8')
ls = [['班级','姓名'],['net221','ab'],['net221','ac'],
      ['net221','ad'],['net221','ae'],['net221','af'],
      ['net221','ag'],['net221','ah'],['net221','al']]
for i in ls:
    file.write(','.join(i) + '\n')
    print(','.join(i)+ '\n')
file.close()