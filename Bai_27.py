import os
os.system('cls')

X = input().strip()
Y = input().strip()

pos = -1
for i in range(len(X) - len(Y) + 1): # i chạy từ 0 đến len(X) - len(Y) -> range phải + 1
    if X[i : i + len(Y)] == Y:
        pos = i + 1

print(pos)


# Input: kmalovekma
#        kma
# i = 0 -> X[0:3] = kma -> pos = 1
# i = 1 -> X[1:4] = mal
# i = 2 -> X[2:5] = alo
# i = 3 -> X[3:6] = lov
# i = 4 -> X[4:7] = ove
# i = 5 -> X[5:8] = vek
# i = 6 -> X[6:9] = ekm
# i = 7 -> X[7:10] = kma -> pos = 8 