import os
os.system('cls')
import math
 #lỗi output
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
    
def cộng_điểm(p, a, x1, y1, x2, y2):
    if x1 == x2 and y1 + y2 == 0:
        #Trương hợp P + Q = O(0,0)
        return (0,0)
    
    if x1 != x2 or y1 != y2:
        #Truong hop P != Q
        tuSo = (y2 - y1) % p
        mauSo = (x2 - x1) % p
        inv = inversion_in_Fp(mauSo, p)
        gamma = (tuSo * inv) % p
    else:
        #Truong hop P = Q
        tuSo = (3 * x1 * x1 + a) % p
        mauSo = (2 * y1) % p
        inv = inversion_in_Fp(mauSo, p)
        gamma = (tuSo * inv) % p
    
    x3 = (gamma * gamma - x1 - x2) % p
    y3 = (gamma * (x1 - x3) - y1) % p
    return x3 , y3

def solve(p, a, Gx, Gy, n):
    Rx, Ry = Gx, Gy
    for _ in range (n - 1):
        Rx, Ry = cộng_điểm(p, a, Rx, Ry, Gx, Gy)
    return Rx, Ry

p = int(input())
a = int(input())
b = int(input())
Gx, Gy = map(int, input().split())
n = int(input())

res = solve(p, a, Gx, Gy, n)

print(f"{res[0]} {res[1]}")