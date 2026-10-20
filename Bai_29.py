import os
os.system('cls')

def LastOccur(pattern, alphabet): # Trả về vị trí xuất hiện cuối cùng
    last = {} # Tạo bảng vị trí xuất hiện cuối cùng của từng ký tự trong pattern
    for char in alphabet:
        last[char] = -1 # Ký tự không có trong pattern
    for i in range(len(pattern)):
        last[pattern[i]] = i
    return last

def BoyerMoore(text, pattern):
    # Tìm vị trí đầu tiên của pattern trong text sử dụng thuật toán Boyer-Moore
    if len(pattern) == 0:
        return 0 # Pattern rỗng khớp tại vị trí đầu

    alphabet = set(text)
    last = LastOccur(pattern, alphabet)
    
    i = len(pattern) - 1  # Chỉ số của text
    j = len(pattern) - 1  # Chỉ số của pattern

    while i < len(text):
        if text[i] == pattern[j]:
            if j == 0:
                return i  # Khớp hoàn toàn
            i -= 1
            j -= 1
        else:
            l = last.get(text[i], -1)
            i += len(pattern) - min(j, 1 + l)
            j = len(pattern) - 1  # Reset pattern pointer về cuối 

    return -1  # Không tìm thấy

def solve(s,t):
    res = list(s)
    while True:
        pos = BoyerMoore("".join(res), t)
        if pos == -1:
            break
        for i in range(pos, pos + len(t)):
            res[i] = '*' # Đánh dấu xóa
    return ''.join(char for char in res if char != '*')

s = input().strip()
t = input().strip()
print(solve(s,t))