import math
import os
os.system('cls')

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
        return "NOT FOUND"
    else:
        d, x, y = euclid_moRong(a,p)
        x = (x % p + p) % p  # đảm bảo x không âm
        return x

p = int(input())
a = int(input())

res = inversion_in_Fp(a, p)
if not inversion_in_Fp(a, p):
    print("NOT FOUND")
else:
    print(res)