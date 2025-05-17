movies = {}
print("欢迎进入鱼C影评小程序")
print("1.数据录入")
print("2.查询数据")
print("3.退出程序")
op = int(input("请输入想要的功能(1/2/3)："))
while op != 3:
    if op == 1:
        go = True
        while go:
            movie = input("请输入电影名称：")
            date = input("请输入上映日期：")
            directors = [ i.strip() for i in input("请输入导演名字（多人请用 / 分隔）：").split("/")]
            actors = [j.strip for j in input("请输入演员名字（多人请用 / 分隔）：").split("/")]
            scores = input("请输入电影评分：")
            movies[movie] = [date, directors, actors, scores]
            if 'N' == input("请问是否继续录入(Y/N):"):
                go = False
    if op == 2:
        name = input("请输入电影名称：")
        if name in movies:
            print(f"电影名称：{name}")
            print(f"上映日期：{movies[name][0]}")
            print(f"导演名单：{movies[name][1]}")
            print(f"演员名单：{movies[name][2]}")
            print(f"当前评分：{movies[name][3]}")
        else:
            print("查无此片！")
    op = int(input("\n请输入想要的功能(1/2/3)："))