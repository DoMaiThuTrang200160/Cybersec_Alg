import os
os.system('cls')

def VetCan(text, pattern):
    i = 0
    res = []
    while i <= len(text) - len(pattern):
        j = 0
        while j < len(pattern):
            if pattern[j] != text[j + i]:
                break
            j += 1
        if j == len(pattern):
            res.append(i)
        i += 1
    return res

s = input()
danh_dau = [0] * len(s)

def solve(word):
    res = VetCan(s, word)
    for pos in res:
        for i in range(pos, pos + len(word)):
            if i < len(danh_dau): # Ít xảy ra TH này, nhưng để tránh lỗi IndexError
                danh_dau[i] = 1

n = int(input())
words = [input() for _ in range(n)]
for word in words:
    solve(word)

result = []
i = 0
while i < len(s):
    if danh_dau[i]:
        result.append("<b>")
        while i < len(s) and danh_dau[i]:
            result.append(s[i])
            i += 1
        result.append("</b>")
    else:
        result.append(s[i])
        i += 1

print(''.join(result))


# Input: abcxyz123
#        2
#        abc 
#        123
# text = "abcxyz123", patterns = ["abc", "123"] -> VetCan("abcxyz123", "abc") trả về [0], VetCan("abcxyz123", "123") trả về [6]
# -> danh_dau = [1, 1, 1, 0, 0, 0, 1, 1, 1] -> kết quả là "<b>abc</b>xyz<b>123</b>"