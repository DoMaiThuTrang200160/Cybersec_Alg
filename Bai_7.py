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

p = int(input())
g = int(input())
x = int(input())

res = mod_pow(g, x, p)
print(res)