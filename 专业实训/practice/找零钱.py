money = int(input())
fen5 = money // 5
money = money % 5
fen2 = money // 2
money = money % 2
fen1 = money // 1
print(f"fen5:{fen5}, fen2:{fen2}, fen1:{fen1}, total:{fen5+fen2+fen1}")     