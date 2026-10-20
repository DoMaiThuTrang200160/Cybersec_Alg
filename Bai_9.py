import os
os.system('cls')

def pow_build(base, mu, mod):
    res = 1
    base %= mod
    while mu > 0:
        if mu % 2 == 1:
            res = (res * base) % mod
        base = (base * base) % mod
        mu //= 2
    return res

p = int(input())
g = int(input())
x = int(input())
a,b = map(int, input().split())

m = (b * pow_build(a, p - 1 - x, p)) % p # Định lý Fermat nhỏ: a^-x = a^(p-1-x) mod p
print(m)

