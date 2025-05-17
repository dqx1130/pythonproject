def judge(password):
    rank = 0
    nums_judge = True
    word1_judge = True
    word2_judge = True
    if len(password) >= 8:
        rank += 1
    nums = "0123456789"
    word1 = "qwertyuiopasdfghjklzxcvbnm"
    word2 = "QWERTYUIOPASDFGHJKLZXCVBNM"
    for each in password:
        if nums_judge:
            if each in nums:
                nums_judge = False
                rank += 1
        if word1_judge:
            if each in word1:
                word1_judge = False
                rank += 1
        if word2_judge:
            if each in word2:
                word2_judge = False
                rank += 1
    return rank


password=input()
print("密码{}强度为{}".format(password,judge(password)))