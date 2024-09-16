import gmpy2
p =gmpy2.mpz(473398607161)
q =gmpy2.mpz(4511491)
e =gmpy2.mpz(17)
phi_n= (p - 1) * (q - 1)
d = gmpy2.invert(e, phi_n)
print("d is:")
print (d)