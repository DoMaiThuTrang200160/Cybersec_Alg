import os
os.system('cls')

def LastOccur(pattern, alphabet):
    last = {}
    for char in alphabet:
        last[char] = -1 # Ký tự không có trong pattern
    for i in range(len(pattern)):
        last[pattern[i]] = i
    return last

def BoyerMoore(text, pattern):
    if len(pattern) == 0:
        return 0 # Pattern rỗng khớp tại vị trí đầu

    alphabet = set(text)
    last = LastOccur(pattern, alphabet)
    
    i = len(pattern) - 1 # Chỉ số của text
    j = len(pattern) - 1 # Chỉ số của pattern

    while i < len(text):
        if text[i] == pattern[j]:
            if j == 0:
                return i # Khớp hoàn toàn
            i -= 1
            j -= 1
        else:
            l = last.get(text[i], -1)
            i += len(pattern) - min(j, 1 + l)
            j = len(pattern) - 1 # Reset pattern pointer

    return -1 # Không tìm thấy

def min_repeat(A, B):
    repeated = ""
    cnt = 0
    while len(repeated) < len(A) + len(B): # Đảm bảo B có thể gối lên 2 lần lặp của A
        cnt += 1
        repeated += A # Ghép nối A vào chuỗi lặp
        if BoyerMoore(repeated, B) != -1:
            return cnt
    return -1

A = input()
B = input()

res = min_repeat(A, B)
print(res)