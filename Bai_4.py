import os

def mod_pow(base, exp, mod):
    res = 1
    base %= mod
    while exp > 0: 
        if exp % 2 == 1:
            res = (res * base) % mod
        base = (base * base) % mod
        exp //= 2
    return res

os.system('cls')

p, g = map(int, input().split())
a, b = map(int, input().split())

A = mod_pow(g, a, p)
K = mod_pow(A, b, p)
print(K)