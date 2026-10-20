import os

os.system('cls')
k = int(input())
n = int(input())

arr = []
for _ in range(n):
    arr.append(input())

str_sample = input()

count = 0

if len(str_sample) < k: # Chuỗi mẫu không thể ngắn hơn tiền tố k
    print(0)
    exit()

prefix_str = str_sample[:k]
print(prefix_str)

for s in arr:
    if len(s) >= k: # Chuỗi phải đủ dài để lấy k ký tự làm tiền tố
        current_prefix = s[:k]
        if current_prefix == prefix_str:
            count += 1

print(count)


# Input: 3 
#        6 
#        abba 
#        abbb 
#        abbc 
#        abbd  
#        abaa 
#        abca 
#        abbg 
# s = abba -> cur_pre = abb -> count++
# s = abbb -> cur_pre = abb -> count++
# s = abbc -> cur_pre = abb -> count++
# s = abbd -> cur_pre = abb -> count++
# s = abaa -> cur_pre = aba
# s = abca -> cur_pre = abc