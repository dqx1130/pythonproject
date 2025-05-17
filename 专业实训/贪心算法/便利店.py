A,B,C,D = map(int,input().split())
N = int(input())
#2L的最低价
min_2L =  min( A * 8 , B * 4 , C * 2 , D)
#1L的最低价
min_1L =  min( A * 4 , B * 2 , C )
money = (N // 2 * min_2L) + ((N % 2) * min_1L)
print(money)