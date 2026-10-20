import os
os.system('cls')

def soSanh_2_chuoi(a, b):
    dicta = dict()
    dictb = dict()
    for i in a:
        if i not in dicta:
            dicta[i] = 1
        else:
            dicta[i] += 1 
    
    for i in b:
        if i not in dictb:
            dictb[i] = 1
        else:
            dictb[i] += 1
    
    return dicta == dictb

s = input().strip()
p = input().strip()
for i in range(len(s) - len(p) + 1): # i chạy từ 0 đến len(s) - len(p) -> range phải + 1
    if soSanh_2_chuoi(s[i : i + len(p)], p):
        print(i, end = ' ')


# Input: BACDGABCDA
#        ABCD
# s[0:4] = "BACD" -> thỏa mãn -> vị trí: 0
# s[1:5] = "ACDG" -> không thỏa mãn
# s[2:6] = "CDGA" -> không thỏa mãn
# s[3:7] = "DGAB" -> không thỏa mãn
# s[4:8] = "GABC" -> không thỏa mãn
# s[5:9] = "ABCD" -> thỏa mãn -> vị trí: 5
# s[6:10] = "BCDA" -> thỏa mãn -> vị trí: 6