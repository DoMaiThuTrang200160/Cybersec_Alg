import os
os.system('cls')

def count_101(s):
    cnt = 0
    for i in range(len(s)):
        if s[i] == '1':
            j = i + 1
            while j < len(s) and s[j] == '0':
                j += 1
            if j > i + 1 and j < len(s) and s[j] == '1': # Đảm bảo có tối thiểu 1 '0' giữa 2 '1', chưa vượt quá độ dài chuỗi và kết thúc bằng '1'
                cnt += 1
    return cnt

s = input()
print(count_101(s))


# Input: 100001abc101
# i = 0, s[0] = '1' -> j = 1, s[1] = '0'
#                      j = 2, s[2] = '0'
#                      j = 3, s[3] = '0'
#                      j = 4, s[4] = '0'
#                      j = 5, s[5] = '1' -> cnt++
# i = 9, s[9] = '1' -> j = 10, s[10] = '0'
#                      j = 11, s[11] = '1' -> cnt++