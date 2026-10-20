import os

def solve(s, goal):
    for i in range(len(s)): # Tối đa lặp len(s) lần vì xoay len(s) lần sẽ về trạng thái ban đầu
        ch = ''
        ch += s[0]
        s = s[:0] + s[1:] + ch # Xoay chuỗi s sang trái 1 ký tự
        # Tường minh các bước xử lý chuỗi, tối ưu hơn  dòng trên: s = s[1:] + s[0]

        if s == goal:
            return True

    return False

os.system('cls')

s = input()
goal = input()

if solve(s, goal):
    print('true')
else:
    print('false')


# Input: abcde
#        cdeab
# ch = 'a' -> s[1:] = 'bcde' -> s = 'bcdea' -> False
# ch = 'b' -> s[1:] = 'cdea' -> s = 'cdeab' -> True
