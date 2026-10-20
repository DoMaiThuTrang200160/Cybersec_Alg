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
        a = random.randrange(2, n - 1)
        if pow_build(a, n - 1, n) != 1:
            return False
    return True

def solve(N):
    check = set() # Dùng set để loại bò trùng lắp
    for n in (arr):
        if isPrime_byFermat(n) and n not in check:
            print(n, end = ' ')
            check.add(n)


N = int(input())
arr = list(map(int, input().split()))

solve(arr)