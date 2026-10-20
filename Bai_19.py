import os
os.system('cls')
import random

def pow_build(base, mu, mod):
    res = 1
    base %= mod
    while mu > 0:
        if mu %2 == 1:
            res = (res * base) % mod
        base = (base * base) % mod
        mu //= 2
    return res

def miller_rabbin(n, k = 5):

    if n == 2 or n == 3:
        return True
    if n <= 1 or n % 2 == 0:
        return False
    
    # Viết n-1 = 2^r * s
    r, s = 0, n - 1
    while s % 2 == 0:
        r += 1
        s //= 2
    for _ in range (k):
        a = random.randrange(2, n - 1)
        x = pow_build(a, s, n)      
        if x == 1 or x == n - 1:
            continue
        for _ in range(r - 1):
            x = pow_build(x, 2, n)
            if x == n - 1:
                break
        else:
            return False
    return True # Nếu qua tất cả lần ktra

def solve(a, b):
    sum = 0
    for n in range(a, b + 1):
        if miller_rabbin(n):
            sum += n
    print(sum)

a = int(input())
b = int(input())

solve(a,b)
    