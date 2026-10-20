import os

def match(word, P):
    j = 0
    for c in word:
        if j < len(P) and c == P[j]: # Đảm bảo chữ in hoa trong từ trùng pattern P theo thứ tự
            j += 1 
        elif c.isupper():
            return False
    return j == len(P) # Đảm bảo pattern khớp toàn bộ

def solve(words, P):
    return [match(q, P) for q in words] # Trả về danh sách kết quả so sánh
    # Không dùng list comprehension thì: 
    # res = []
    # for q in words:
    #     res.append(match(q, P))
    # return res

os.system('cls')

n = int(input())
words = [input() for _ in range(n)]
P = input()

res = solve(words, P)
# print(res)
for check in res:
    if check:
        print('true')
    else:
        print('false')


# Input: 5
#        FooBar
#        FooBarTest
#        FootBall
#        FrameBuffer
#        ForceFeedBack
#        FB
# P = 'FB'
# word = 'FooBar' -> match = True
# word = 'FooBarTest' -> match = False do thừa ký tự 'T'
# word = 'FootBall' -> match = True
# word = 'FrameBuffer' -> match = True
# word = 'ForceFeedBack' -> match = False do thừa ký tự 'F'