import os
os.system('cls')

def pow_buid(base, mu, mod):
    res = 1
    base %= mod
    while mu > 0:
        if mu % 2 == 1:
            res = (res * base) % mod
        base = (base * base) % mod
        mu //= 2
    return res

p = int(input())
q = int(input())
m = int(input())
d = int(input())
n = p * q
s = pow_buid(m, d, n)

print(s)