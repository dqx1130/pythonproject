import random
def paiku(database):
    for i in ['♦','♥','♠','♣']:
        for j in ['A','J','Q','K','2','3','4','5','6','7','8','9','10']:
            result = i + j
            database.append(result)
    database.append("大王")
    database.append("小王")
    # print(database)
    return database
def main():
    database =[]
    paiku(database)
    first_player = input("请输入第一位游戏玩家名称：")
    second_player = input("请输入第二位游戏玩家名称：")
    third_player = input("请输入第三位游戏玩家名称：")
    #叫地主
    whoisdizhu = random.randint(1,3)
    if whoisdizhu == 1:
        print(f"地主是玩家{first_player}")
    elif whoisdizhu == 2:
        print(f"地主是玩家{second_player}")
    elif whoisdizhu == 3 :
        print(f"地主是玩家{third_player}")
    #抽牌
    judge = len(database)
    player = 1
    player_1 = []
    player_2 = []
    player_3 = []
    while judge > 3:
        pai_index = random.randint(0,judge-1)
        pai = database[pai_index]
        # print(pai)
        #发牌
        if player > 3:
            player = 1
        if player == 1:
            player_1.append(pai)
        elif player == 2:
            player_2.append(pai)
        elif player == 3:
            player_3.append(pai)
        #牌已发，删牌
        database.remove(pai)
        judge -= 1
        player += 1
    #发地主牌
    for each in database:
        if whoisdizhu == 1:
            player_1.append(each)
        elif whoisdizhu == 2:
            player_2.append(each)
        elif whoisdizhu == 3:
            player_3.append(each)
    print(f"[{first_player}]拿到的牌是：{player_1}")
    print(f"[{second_player}]拿到的牌是：{player_2}")
    print(f"[{third_player}]拿到的牌是：{player_3}")

if __name__ == '__main__':
    main()
