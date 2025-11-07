ciphertext = ['96', '65', '93', '123', '91', '97', '22', '93', '70', '102', '94', '132', '46', '112', '64', '97', '88',
              '80', '82', '137', '90', '109', '99', '112']
ciphertext = ciphertext[::-1]
flag = ''
for i in range(len(ciphertext)):
      if (i % 2 == 0):
            a = int(ciphertext[i]) - 10
      else:
            a = int(ciphertext[i]) + 10
      a = i ^a
      flag = flag + chr(a)
print(flag)
