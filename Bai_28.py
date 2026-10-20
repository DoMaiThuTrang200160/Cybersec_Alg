import os
os.system('cls')

def bad_or_gud(s):
    nguyenAm = set('aeiou')
    nguyenAm_lienTiep = phuAm_lienTiep = 0

    for ch in s:
        if ch in nguyenAm:
            nguyenAm_lienTiep +=1
            phuAm_lienTiep = 0
        elif ch != '?':
            phuAm_lienTiep +=1
            nguyenAm_lienTiep = 0
        else:  # ch == '?'
            nguyenAm_lienTiep +=1
            phuAm_lienTiep +=1
        
        if nguyenAm_lienTiep >= 6 or phuAm_lienTiep >= 4:
            return "BAD"
    return "GOOD"

s = input()
print(bad_or_gud(s))


# Input: aeioup??
# ch = 'a' -> nguyenAm_lienTiep = 1, phuAm_lienTiep = 0
# ch = 'e' -> nguyenAm_lienTiep = 2, phuAm_lienTiep = 0
# ch = 'i' -> nguyenAm_lienTiep = 3, phuAm_lienTiep = 0
# ch = 'o' -> nguyenAm_lienTiep = 4, phuAm_lienTiep = 0
# ch = 'u' -> nguyenAm_lienTiep = 5, phuAm_lienTiep = 0
# ch = 'p' -> nguyenAm_lienTiep = 0, phuAm_lienTiep = 1
# ch = '?' -> nguyenAm_lienTiep = 1, phuAm_lienTiep = 2
# ch = '?' -> nguyenAm_lienTiep = 2, phuAm_lienTiep = 3