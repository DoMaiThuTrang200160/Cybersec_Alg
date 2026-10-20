import os
os.system('cls')
import math

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

def ORD(a, n):
    t = 1
    while True:
        if pow_build(a, t, n) == 1:
            return t
        else:
            t += 1

n = int(input())
a = int(input())
b = int(input())

m = math.ceil(math.sqrt(ORD(a, n)))
ajn = []
bian = []
for j in range(m):
    ajn.append(pow_build(a, j, n))
    z = (b * inversion_in_Fp(pow_build(a, m * j, n), n)) % n
    bian.append(z)
i_tm, j_tm = -1, -1 # Đánh dấu chưa tìm thấy giá trị phù hợp

for j, valuej in enumerate(ajn):
    for i, valuei in enumerate(bian):
        if valuei == valuej:
            i_tm = i
            j_tm = j
            break
print(m * i_tm + j_tm)