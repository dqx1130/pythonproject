def CountDigit(number,digit):
    number = abs(number)
    number = str(number)
    digit = str(digit)
    count = 0
    for each in number:
        if each == digit:
            count +=  1
    return count


# number,digit=input().split()
# number=int(number)
# digit=int(digit)
number = -21252
digit = 2
count=CountDigit(number,digit)
print("Number of digit 2 in "+str(number)+":",count)