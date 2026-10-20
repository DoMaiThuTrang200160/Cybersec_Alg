import math
import os
os.system('cls')
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

def isPrime_byFermat(n, k = 5):
    if n <= 1:
        return False
    if n == 2 or n == 3:
        return True
    
    for _ in range(k):
        a = random.randrange(2, n - 1) # Tăng độ tin cậy và hiệu quả phát hiện hợp số
        if pow_build(a, n - 1, n) != 1:
            return False
    return True

def prime_in_range(a, b):
    sum = 0
    for n in range(a, b + 1):
        if isPrime_byFermat(n):
            sum += n
    print(f"{sum}")

a = int(input())
b = int(input())

prime_in_range(a, b)