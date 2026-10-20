import os
os.system('cls')

def BoolRepeatedSubstring(s):
    for i in range(1, len(s) // 2 + 1): # Chuỗi phải do tối thiểu 2 chuỗi con lặp lại tạo thành
        if len(s) % i == 0: # Chuỗi do lặp k lần, tức len(s) = k * i
            sub = s[:i]
            if sub * (len(s) // i) == s:
                return "YES"
    return "NO"

s = input().strip()
print(BoolRepeatedSubstring(s))

# Input: ababab -> n = 6 -> duyệt từ 1 tới 3
# i = 1: sub = 'a' -> 'a' * 6 == 'aaaaaa' -> NO
# i = 2: sub = 'ab' ->'ab' * 3 == 'ababab' -> YES 