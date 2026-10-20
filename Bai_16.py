import os
os.system('cls')

def pow_build(base, mu, mod):
    res = 1
    base %= mod
    while mu > 0:
        if mu % 2 == 1:
            res = (res * base) % mod
        base=(base * base) % mod
        mu //= 2
    return res

def isPrime_tested_byFermat(n):
    if n <= 1:
        return False
    if n == 2 or n == 3:
        return -1
    for i in range(t):
        a = am[i]
        if pow_build(a, n - 1, n) != 1:
            return i + 1
    return -1

n = int(input())
t = int(input())
am = []
for i in range(t):
    a = int(input())
    am.append(a)

res = isPrime_tested_byFermat(n)
print(res)
