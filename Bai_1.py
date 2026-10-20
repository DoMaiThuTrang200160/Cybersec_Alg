import os
import math
os.system('cls')

def euclid_moRong(a, b):    # a⋅x+b⋅y=gcd(a,b)=d
    if b == 0:        # gcd(a,b)=0
        d, x, y = a, 1, 0
        return d, x, y

    x2, x1 = 1, 0
    y2, y1 = 0, 1

    while b > 0:
        q, r = divmod(a, b)
        x, y = x2 - q * x1, y2 - q * y1
        a, b = b, r
        x2, x1 = x1, x       # Cập nhật giá trị cho vòng lặp sau
        y2, y1 = y1, y       # Vòng lặp sẽ tiếp tục cho tới khi b = 0 ⇒ khi đó a chính là gcd(a,b).

    d, x, y = a, x2, y2
    return d, x, y

def inversion_in_Fp(a, p):
    if math.gcd(a, p) != 1:    # a, p ko nguyên tố
        return False
    else:
        d, x, y = euclid_moRong(a,p)
        x = (x % p + p) % p  # Đảm bảo x không âm (x phải là số nguyên dương nhỏ hơn p)
        return x

p = int(input())
q = int(input())
e = int(input())

n = p * q
phi_n = (p - 1) * (q - 1)
d = inversion_in_Fp(e, phi_n)

print(n)
print(d)