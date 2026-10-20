import os
os.system('cls')
import math
import random

def pow_build(base, mu, mod):
    res = 1
    base %= mod
    while mu > 0:
        if mu % 2 == 1:
            res = (res * base) % mod
        base = (base * base) % mod
        mu //= 2
    return res

def euclid_moRong(a, b):
    if b == 0:
        d, x, y = a, 1, 0
        return d, x, y

    x2, x1 = 1, 0
    y2, y1 = 0, 1

    while b > 0:
        q, r = divmod(a, b)
        x, y = x2 - q * x1, y2 - q * y1
        a, b = b, r
        x2, x1 = x1, x
        y2, y1 = y1, y

    d, x, y = a, x2, y2
    return d, x, y

def inversion_in_Fp(a, p):
    if math.gcd(a, p) != 1:
        return False
    else:
        d, x, y = euclid_moRong(a,p)
        x = (x % p + p) % p  # đảm bảo x không âm
        return x

p = int(input())
alpha = int(input())
a = int(input())
# b = int(input())
k = int(input())
x = int(input())

gamma = pow_build(alpha, k, p)
rô1 = (x - a * gamma) % (p - 1)
rô2 = inversion_in_Fp(k, p - 1)
rô = (rô1 * rô2) % (p - 1)

print(gamma, rô)