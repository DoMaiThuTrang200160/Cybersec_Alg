import os
os.system('cls')

def pow_build(base, mu, mod):
    res = 1
    base %= mod # Giảm kích thước
    while mu > 0:
        if mu % 2 == 1:
            res = (res * base) % mod
        base = (base * base) % mod  
        mu //= 2  # Gạch bit cuối
    return res 

p = int(input())
q = int(input())
e = int(input())
m = int(input())

n = p * q
phi_n = (p - 1) * (q - 1)
c = pow_build(m, e, n)

print(c)