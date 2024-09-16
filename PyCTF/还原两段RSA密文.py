from Crypto.PublicKey import RSA
from Crypto.Util.number import *

c = 6945004599188163993695415369835695903301224003136994252560594956191090963121611565339316899123749651980866032846579298200421747380583546633355992903073674181349057044030322829788264132202636849376954935277228938532451604402772829242424577058024238656161078439246537271516326863255516855631753446705292842229626286876548916801469642547513456705866784202623394305276451128865785358297012288872815722144655832856702699498675579782594166664458814522864775862036884859354259378908758433643337060342583622920263235497780709801069090899910257671959718315799533292405361650450010152269010240983236777594133358567962307235569

s = 2657375403899004421682435875591648757169751001935445937761677813563331237751296771655965799410203548200444843121899114276425174188686046977514392352233441829494629361400810323413751538449142557000621910082199277027187814332458889139635831754705831808451385798544850324418189973193940364270700678684371080465070928269782397410454121628205746311654719735981174781630012234885865191874665887323338400055601894791632973447395440378983992188376105785566869556895986983889219094640854379267584790389009829385657891279182819588524435817909919666674804622368593843455996806164859962400637898116212711639490474051288221345806

with open(r'C:\Users\Administrator\Desktop\priv.pem') as f:
    pk = RSA.importKey(f.read())    #私钥

m = pow(c, pk.d, pk.n)              #pow(底数,指数,取余数字)
                                    #pow(c,私钥.d,私钥.n)
                                    # 这是一个Python Cryptography Toolkit (pycrypto)中RSA密钥类的属性。
                                    # 该属性表示RSA私钥参数d，是一个整数类型（int）。
                                    # 它指定了RSA算法在解密和签名操作中使用的私钥参数。
                                    # 由于这是一个只读属性（@property），
                                    # 因此无法直接修改d的值，
                                    # 但可以通过创建新的RSA私钥来生成具有不同d值的新密钥。
print(long_to_bytes(m))

cc = pow(s, pk.e, pk.n)

print(long_to_bytes(cc))