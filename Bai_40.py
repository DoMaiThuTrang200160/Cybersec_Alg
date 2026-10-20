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

n = int(input())
words = [input() for _ in range(n)]

res = []

for i in range(n):
    for j in range(n):
        if i != j and VetCan(words[j], words[i]): # Ko so sánh i == j vì nvay word[i] sẽ so sánh vs chính nó -> bỏ qua
            res.append(words[i])
            break  

if res:
    print(' '.join(res))
else:
    print("None")


# Input: mass
#        as
#        hero
#        superhero
# pattern: mass, còn lại là text -> hàm VetCan trả về False
# pattern: as, còn lại là text -> hàm VetCan trả về True với TH text = "mass", các TH khác trả về False
# pattern: hero, còn lại là text -> hàm VetCan trả về True với TH text = "superhero", các TH khác trả về False
# pattern: superhero, còn lại là text -> hàm VetCan trả về False