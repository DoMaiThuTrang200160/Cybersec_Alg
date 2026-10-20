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

def miller_rabbin(n, j_max, a):
    if n == 2 or n == 3:
        return True
    if n <= 1 or n % 2 == 0:
        return False
    # Phân tích n-1 = 2^r * s ( s là số lẻ)
    r = n - 1
    s = 0
    while r % 2 == 0:
        r //= 2
        s += 1

    y = pow_build(a, r, n)
    for _ in range (1):
        if y != 1 and y != n - 1:
            j = 1
            if j_max > s - 1:
                print(f"Too manny steps")
            while j <= j_max and y != n - 1:
                y = pow_build(y, 2, n)
                if y == 1:
                    return y
                j += 1
            if y != n - 1:
                return y
    return 1


n = int(input())         
a = int(input())         
j_max = int(input())     


print(f'{miller_rabbin(n, j_max, a)}')
