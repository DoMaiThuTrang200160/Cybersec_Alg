import os
os.system('cls')
import math

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
        d, x, y = euclid_moRong(a, p)
        x = (x % p + p) % p  # đảm bảo x không âm
        return x

k = int(input())
a = []
for i in range (k):
    ai, ni = map(int, input().split())
    a.append([ai, ni])

N = 1
for xi, ni in a:
    N *= ni

for item in a:
    ai, ni = item[0], item[1]
    Ni = N // ni # Tích các modulo khác ni
    Mi = inversion_in_Fp(Ni, ni)
    item.append(Ni)
    item.append(Mi)

x = 0
for item in a:
    ai, ni, Ni, Mi = item
    x = (x + ai * Ni * Mi) % N

print(x)