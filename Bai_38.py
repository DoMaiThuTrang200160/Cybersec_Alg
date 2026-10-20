import os
os.system('cls')

def VetCan(text, pattern):
    i = 0
    while i <= len(text) - len(pattern):
        j = 0
        while j < len(pattern):
            if pattern[j] != text[j + i]:
                break
            j += 1
        if j == len(pattern):
            return True
        i += 1
    return False

sequence = input().strip()
word = input().strip()

k = 0
while True:
    k += 1
    new_word = word * k
    if not VetCan(sequence, new_word):
        break

if k > 1:
    print(f'{k - 1}')     #in k-1 vì lần cuối ko đúng


#Input:ababc
#      ab
#Lặp:
#k=1 → "ab" có trong "ababc" → tiếp tục
#k=2 → "abab" có trong "ababc" → tiếp tục
#k=3 → "ababab" không có trong "ababc" → dừng
#→ Output: 2