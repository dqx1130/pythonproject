ipsort=[
  ['10', '51', '3', '31'],
  ['10', '41', '2', '15'],
  ['152', '222', '55', '1'],
  ['15', '5', '64', '22'],
  ['123', '213', '25', '11']
]

for i in range(len(ipsort)):
    for j in range(len(ipsort[i])):
        ipsort[i][j] = int(ipsort[i][j])
        print(ipsort)