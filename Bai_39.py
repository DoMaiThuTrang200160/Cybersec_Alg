import os
os.system('cls')

def VetCan(text, pattern):
    i = 0
    while i <= len(text) - len(pattern):
        j = 0
        while j < len(pattern):
            if pattern[j] != text[j + i]:
                break
            j += 1
        if j == len(pattern):
            return True
        i += 1
    return False

sentence = input().strip()
searchWord = input().strip()

words = sentence.split() # Tách chuỗi thành danh sách các từ theo dấu cách

for idx, word in enumerate(words): # Sd enumerate để duyệt qua từng word và lấy index của chúng
    if VetCan(word, searchWord):
        print(idx + 1) # idx + 1 vì đề yêu cầu bắt đầu từ 1
        break
else:
    print(-1)


# Input: i love eating burger 
#        burg
# idx == 0 -> word = "i" -> VetCan("i", "burg") -> False
# idx == 1 -> word = "love" -> VetCan("love", "burg") -> False
# idx == 2 -> word = "eating" -> VetCan("eating", "burg") -> False
# idx == 3 -> word = "burger" -> VetCan("burger", "burg") -> True