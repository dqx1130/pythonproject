# Corrected Pure Python Code
from Crypto.Util.number import long_to_bytes

def legendre_symbol(a, p):
    """
    Calculates the Legendre symbol (a/p).
    Returns 1 if a is a quadratic residue modulo p, -1 if it is a non-residue,
    and 0 if a is divisible by p.
    """
    ls = pow(a, (p - 1) // 2, p)
    if ls == p - 1:
        return -1
    return ls

def tonelli_shanks(n, p):
    """
    Tonelli-Shanks algorithm to find the modular square root of n modulo p.
    This works for any prime p.
    """
    if legendre_symbol(n, p) != 1:
        return None  # n is not a quadratic residue

    if p % 4 == 3:
        return pow(n, (p + 1) // 4, p)

    # Decompose p-1 into Q * 2^S
    Q = p - 1
    S = 0
    while Q % 2 == 0:
        Q //= 2
        S += 1

    if S == 1:
        return pow(n, (p + 1) // 4, p)

    # Find a quadratic non-residue z
    z = 2
    while legendre_symbol(z, p) != -1:
        z += 1

    M = S
    c = pow(z, Q, p)
    t = pow(n, Q, p)
    R = pow(n, (Q + 1) // 2, p)

    while t != 1:
        if t == 0:
            return 0
        i = 0
        temp_t = t
        while temp_t != 1:
            temp_t = (temp_t * temp_t) % p
            i += 1
            if i == M:
                return None

        b = pow(c, pow(2, M - i - 1, p - 1), p)
        M = i
        c = (b * b) % p
        t = (t * c) % p
        R = (R * b) % p

    return R

# The rest of the script is the same
p = 9620154777088870694266521670168986508003314866222315790126552504304846236696183733266828489404860276326158191906907396234236947215466295418632056113826161
C_list = [
    [7062910478232783138765983170626687981202937184255408287607971780139482616525215270216675887321965798418829038273232695370210503086491228434856538620699645, 7096268905956462643320137667780334763649635657732499491108171622164208662688609295607684620630301031789132814209784948222802930089030287484015336757787801],
    [7341430053606172329602911405905754386729224669425325419124733847060694853483825396200841609125574923525535532184467150746385826443392039086079562905059808, 2557244298856087555500538499542298526800377681966907502518580724165363620170968463050152602083665991230143669519866828587671059318627542153367879596260872]
]

a_val, b_val = C_list[0][0], C_list[0][1]
c_val, d_val = C_list[1][0], C_list[1][1]

tr = (a_val + d_val) % p
det = (a_val * d_val - b_val * c_val) % p

b_eq = -tr % p
c_eq = det

delta = (b_eq*b_eq - 4*1*c_eq) % p
s = tonelli_shanks(delta, p)

if s is not None:
    inv_2 = pow(2, -1, p)
    lambda1 = ((-b_eq + s) * inv_2) % p
    lambda2 = ((-b_eq - s) * inv_2) % p

    print(f"Correct Eigenvalues: [{lambda1}, {lambda2}]")

    part1 = long_to_bytes(lambda1)
    part2 = long_to_bytes(lambda2)

    # Check which one is which part
    if len(part1) > len(part2):
        part1, part2 = part2, part1

    print(f"\nPart 1: {part1}")
    print(f"Part 2: {part2}")

    flag_content = part1 + part2
    print(f"\nFlag content: {flag_content}")

    final_flag = b'LILCTF{' + flag_content + b'}'
    print(f"\nFinal Flag: {final_flag.decode()}")
else:
    print("Could not find the modular square root.")

    # LILCTF{It_w4s_the_be5t_of_times_}