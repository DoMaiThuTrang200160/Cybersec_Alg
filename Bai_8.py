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
k = int(input())
y = int(input())
m = int(input())
a = mod_pow(g, k, p)
print(a)

b = mod_pow(y, k, p)
b = (m * b) % p
print(b)
