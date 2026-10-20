def count(s):
    freq = {} # Tạo dict rỗng đếm tần suất xhien mỗi phần tử
    for ch in s:
        if ch in freq:
            freq[ch] += 1 
        else:
            freq[ch] = 1

    # print(freq)
    count = 0
    for f in freq.values():
        count += f * (f + 1) // 2 # f chuỗi dài 1 ký tự và f * (f - 1) / 2 (tổ hợp chập 2 f vị trí) chuỗi dài từ 2 ký tự trở lên

    return count

import os
os.system('cls')
s = input()
result = count(s)
print(result)


# Input: abcab -> freq = {'a': 2, 'b': 2, 'c': 1} -> count = 2 * (2 + 1) // 2 + 2 * (2 + 1) // 2 + 1 * (1 + 1) // 2 = 3 + 3 + 1 = 7