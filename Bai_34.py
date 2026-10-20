import os
os.system('cls')

def check_tien_to(tu1, tu2, i): # Kiểm tra tiền tố của tu1 và tu2 có giống nhau không
    return tu1[:i] == tu2[:i]

def solve(tu, words):
    i = 1
    while True:
        check = 0 # Gắn biến cờ check tức là chưa trùng
        for word in words:
            if tu == word: # Nếu từ htai là chính nó thì bỏ qua
                continue
            else:
                check = check_tien_to(tu, word, i)
                if check:
                    break
        if check:
            i += 1
        else:
            return tu[:i]

if __name__ == '__main__':
    n = int(input())
    words = [input() for _ in range(n)]
    res = []
    for word in words:
        res.append(solve(word, words))
    print(' '.join(res))


# Input: 4 
#        zebra 
#        dog 
#        duck 
#        dove 
# tu = zebra - > i = 1: 'z' -> lưu lại
# tu = dog - > i = 1: 'd' -> i = 2: 'do' -> i = 3: 'dog' -> lưu lại
# tu = duck - > i = 1: 'd' -> i = 2: 'du' ->  lưu lại
# tu = dove - > i = 1: 'd' -> i = 2: 'do' -> i = 3: 'dov' -> lưu lại