import gmpy2  # 计算大整数模块
import libnum
import rsa
from Crypto.PublicKey import RSA  # 安装时安装pycryptodome模块


# 已知：p，q，e，c
def known_p_q_e_c():
    p = int(input('请输入一个素数p：'))
    q = int(input('请输入另一个素数q：'))
    e = int(input('请输入公钥e：'))
    c = int(input('请输入密文c：'))

    d = gmpy2.invert(e, (p - 1) * (q - 1))
    m = gmpy2.powmod(c, d, p * q)

    return d, m


# 已知：n(较小，不超过256bit)，e，c
def known_nmin_e_c():
    n = int(input('请输入一个整数n：'))
    e = int(input('请输入公钥e：'))
    c = int(input('请输入密文c：'))

    divisor = libnum.factorize(n)  # 因式分解
    p = int(list(divisor.keys())[0])
    q = int(list(divisor.keys())[1])

    d = gmpy2.invert(e, (p - 1) * (q - 1))
    m = gmpy2.powmod(c, d, n)

    print(f'素数p：{p}\n素数q：{q}')

    return d, m


# 已知：n，e1,c1,e2,c2
def known_n_e1_c1_e2_c2():
    n = int(input('请输入一个整数n：'))
    e1 = int(input('请输入公钥e1：'))
    c1 = int(input('请输入密文c1：'))
    e2 = int(input('请输入公钥e2：'))
    c2 = int(input('请输入密文c2：'))

    s, s1, s2 = gmpy2.gcdext(e1, e2)  # 扩展欧几里得算法
    if s1 < 0:
        s1 = - s1
        c1 = gmpy2.invert(c1, n)
    elif s2 < 0:
        s2 = - s2
        c2 = gmpy2.invert(c2, n)
    m = (pow(c1, s1, n) * pow(c2, s2, n)) % n

    return m


# 已知：n，e(非常小)，c
def known_n_emin_c():
    n = int(input('请输入一个整数n：'))
    e = int(input('请输入公钥e：'))
    c = int(input('请输入密文c：'))

    k = 0
    while True:
        m, flag = gmpy2.iroot(c + k * n, e)
        if flag == True:
            return m
        k += 1


# 已知：公钥文件publickey_file
def known_publickey_file():
    publickey_file = input('请输入公钥文件路径：')

    public = RSA.importKey(open(publickey_file).read())  # 公钥解析

    print(f'整数n：{public.n}\n公钥e：{public.e}')


# 已知：加密文件cfile，p，q，e
def known_cflie_p_q_e():
    cfile = input('请输入加密文件路径：')
    p = int(input('请输入一个素数p：'))
    q = int(input('请输入另一个素数q：'))
    e = int(input('请输入公钥e：'))

    d = gmpy2.invert(e, (p - 1) * (q - 1))
    key = rsa.PrivateKey(p * q, e, d, p, q)  # 制定新的密钥对
    m = libnum.s2n(rsa.decrypt(open(cfile, 'rb').read(), key))  # 使用密钥对文件进行解密，再转换成数字

    return d, m


# 已知：p1~pn，e，c
def known_p1_pn_e_c():
    x = int(input('请输入n分解的质因数个数：'))
    list_p = []
    pq = 1
    n = 1

    for index in range(x):
        tmp = int(input(f'请输入质因子p{index + 1}：'))
        list_p.append(tmp)
        pq *= tmp - 1
        n *= tmp

    e = int(input('请输入公钥e：'))
    c = int(input('请输入密文c：'))

    d = gmpy2.invert(e, pq)
    m = gmpy2.powmod(c, d, n)

    return d, m


# 已知：p，q，dp，dq，c
def known_p_q_dp_dq_c():
    p = int(input('请输入一个素数p：'))
    q = int(input('请输入另一个素数q：'))
    dp = int(input('请输入d模(p-1)：'))
    dq = int(input('请输入d模(q-1)：'))
    c = int(input('请输入密文c：'))

    mp = gmpy2.powmod(c, dp, p)
    mq = gmpy2.powmod(c, dq, q)
    m = (((mp - mq) * gmpy2.invert(q, p)) % p) * q + mq

    return m


# 已知：n，e，dp，c
def known_n_e_dp_c():
    n = int(input('请输入一个整数n：'))
    e = int(input('请输入公钥e：'))
    dp = int(input('请输入d模(p-1)：'))
    c = int(input('请输入密文c：'))

    for x in range(1, e):
        if (dp * e - 1) % x == 0:
            if n % (((dp * e - 1) // x) + 1) == 0:
                p = ((dp * e - 1) // x) + 1
                q = n // p
                phi = (p - 1) * (q - 1)

                d = gmpy2.invert(e, phi)
                m = gmpy2.powmod(c, d, n)

                return d, m


# 已知：p+q，(p+1)*(q+1)，d，c
def known_paq_pa1mqa1_d_c():
    paq = int(input('请输入p+q：'))
    pa1mqa1 = int(input('请输入(p+1)*(q+1)：'))
    d = int(input('请输入私钥d：'))
    c = int(input('请输入密文c：'))

    n = pa1mqa1 - paq - 1
    m = gmpy2.powmod(c, d, n)

    return d, m


# 已知：e，n组、c组
def known_e_ngroup_cgroup():
    e = int(input('请输入公钥e：'))
    ngroup = list(map(int, input('请输入n组(空格隔开)：').split()))
    cgroup = list(map(int, input('请输入c组(空格隔开)：').split()))

    for count1 in range(len(ngroup)):
        for count2 in range(len(ngroup)):
            if count1 != count2:
                if gmpy2.gcd(ngroup[count1], ngroup[count2]) != 1 and gmpy2.is_prime(gmpy2.gcd(ngroup[count1], ngroup[count2])):  # 求公因数并为质数
                    p = gmpy2.gcd(ngroup[count1], ngroup[count2])

                    if gmpy2.is_prime(ngroup[count1] // p):  # 只有当p、q都为质数时计算才有意义
                        q = ngroup[count1] // p
                        d = gmpy2.invert(e, (p - 1) * (q - 1))
                        m = pow(cgroup[count1], d, ngroup[count1])

                        return d, m


# 已知：n组(两两互质)、c组
def known_ngroup_cgroup():
    ngroup = list(map(int, input('请输入n组(空格隔开)：').split()))
    cgroup = list(map(int, input('请输入c组(空格隔开)：').split()))
    e_begin = int(input('请输入e的最小范围(不小于2)：'))
    e_finish = int(input('请输入e的最大范围：'))

    N = 1
    for n in ngroup:
        N *= n

    for e in range(e_begin, e_finish):
        m_power_e = 0
        for count in range(len(ngroup)):
            m_power_e += cgroup[count] * N // ngroup[count] * gmpy2.invert(N // ngroup[count], ngroup[count])

        m, flag = gmpy2.iroot(m_power_e % N, e)
        if flag:
            return m


# 已知：p、q、e(与phi不互素)、c
def known_p_q_eprime_c():
    p = int(input('请输入一个素数p：'))
    q = int(input('请输入另一个素数q：'))
    e = int(input('请输入公钥e：'))
    c = int(input('请输入密文c：'))

    n = p * q
    phi = (p - 1) * (q - 1)
    t = gmpy2.gcd(e, phi)
    d = gmpy2.invert(e // t, phi)
    m = pow(c, d, n)

    return int(gmpy2.iroot(m, t)[0])  # 求m开t次根


d = None
m = None

condition = int(input('''已知条件：1、p，q，e，c
        2、n(较小)，e，c
        3、n，e1，c1，e2，c2
        4、n，e(非常小)，c
        5、公钥解析(公钥文件)
        6、加密文件，p，q，e，d
        7、p1~pn(多个质因子)，e，c
        8、p，q，dp，dq，c
        9、n，e，dp，c
        10、p+q，(p+1)*(q+1)，d，c
        11、e，n组、c组
        12、n组(两两互质)、c组
        13、已知：p、q、e(与phi不互素)、c
请输入序号：'''))
if condition == 1:
    d, m = known_p_q_e_c()
elif condition == 2:
    d, m = known_nmin_e_c()
elif condition == 3:
    m = known_n_e1_c1_e2_c2()
elif condition == 4:
    m = known_n_emin_c()
elif condition == 5:
    known_publickey_file()
elif condition == 6:
    d, m = known_cflie_p_q_e()
elif condition == 7:
    d, m = known_p1_pn_e_c()
elif condition == 8:
    m = known_p_q_dp_dq_c()
elif condition == 9:
    d, m = known_n_e_dp_c()
elif condition == 10:
    d, m = known_paq_pa1mqa1_d_c()
elif condition == 11:
    d, m = known_e_ngroup_cgroup()
elif condition == 12:
    m = known_ngroup_cgroup()
elif condition == 13:
    m = known_p_q_eprime_c()
else:
    print('请输入正确的序号！')

print(f'私钥d：{d}')
print(f'明文m：{m}')
if m != None:
    print(f'字符明文：{libnum.n2s(int(m)).decode("utf-8")}')
    # 数字转字符串，再进行utf-8编码




