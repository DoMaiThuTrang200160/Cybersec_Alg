import os
os.system('cls')

s = input().strip()
mid = len(s) // 2 # Tiền tố, hậu tố giống nhau mà không được trùng lấp
length = 0
for i in range(0, mid + 1):
    if s[:i] == s[-i:]:
        length = i
    
print(length)

# Input: aabcdaabc -> len = 9, mid = 4
# i = 1: s[:1] = "a" và s[-1:] = "c" -->"a" != "c"
# i = 4: s[:4] = "aabc" và s[:-4] = "aabc" -->"aabc" == "aabc"