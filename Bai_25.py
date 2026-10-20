import os
os.system('cls')

def solve(s):
    mapping = {} # Tạo 1 từ điển ánh xạ chuỗi s thành chỉ số xuất hiện
    res = []  # Lưu pattern ánh xạ của chuỗi s
    cnt = 0
    for c in s:
        if c not in mapping:
            mapping[c] = cnt
            cnt += 1 # Đảm bảo mỗi ký tự có ánh xạ duy nhất
        res.append(str(mapping[c])) # Thêm theo ánh xạ
    return ' '.join(res)

n = int(input())
ds_hanh_vi = []
for _ in range (n):
    ds_hanh_vi.append(input())

chuoi_doi_sanh = input()

encode_pattern = solve(chuoi_doi_sanh)

res = []
for behavior in ds_hanh_vi:
    if solve(behavior) == encode_pattern:
        res.append(behavior)

print(' '.join(res))


# Input: 4 
#        abb 
#        abc 
#        xyz 
#        xyy 
#        foo
# Chuỗi đối sánh: foo -> pattern: 0 1 1
# Hành vi: abb -> 0 1 1 -> thêm vào dsach
# Hành vi: abc -> 0 1 2 -> không thêm vào dsach
# Hành vi: xyz -> 0 1 2 -> không thêm vào dsach
# Hành vi: xyy -> 0 1 1 -> thêm vào dsach