a = "386f1e24132514513c24b5538a5d281233b5d201e46173d102a4144491a315a"
for i in range(0,len(a),2):
    data = int(a[i:i+2],16)
    print(chr(data),end='')

#由于转化后ascii大于128，所以都减去128