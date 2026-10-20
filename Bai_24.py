import os

def is_match(s, p):
    memo = {}
    def dp(i, j):
        if (i, j) in memo:
            return memo[(i, j)]
        
        if j == len(p):
            return True
        
        if j < len(p) and p[j] == '*':
            # chia làm 2 trường hợp:
            # 1. '*' khớp với chuỗi rỗng, coi như bỏ '*' đi, dp(i, j + 1) 
            # 2. '*' khớp với 1 chuỗi, nếu vẫn chưa xét hết s, dp(i + 1, j)
            res = dp(i, j+1) or (i < len(s) and dp(i+1, j))
        else:
            # kiểm tra xem hiện tại có cặp nào khớp không
            # nếu khớp thì đổi cặp tiếp theo
            match = i < len(s) and (p[j] == s[i] or p[j] == '?')
            res = match and dp(i+1, j+1)
            
        memo[(i, j)] = res
        return res

    for start in range(len(s)):
        if dp(start, 0):
            return True
    return False

os.system('cls')

S = input()
P = input()
print("true" if is_match(S, P) else "false")