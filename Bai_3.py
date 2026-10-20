import os
os.system('cls')

def pow_build(base, mu, mod):
    res = 1
    base %= mod
    while mu > 0:
        if mu % 2 == 1:
            res = (res * base) % mod
        base = (base * base) % mod  
        mu //= 2  # Gạch bit cuối
    return res

p = int(input())
q = int(input())
m = int(input())

n = p * q
if (m < n):
    c = pow_build(m, 2, n)

print(c)