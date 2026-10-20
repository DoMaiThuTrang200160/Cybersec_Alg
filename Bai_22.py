import os
os.system("cls")

def LastOccur(pattern,alphabet):
    last = {}
    for char in alphabet:
        last[char] = -1
    for i in range (len(pattern)):
        last[pattern[i]] = i
    return last

def BoyerMoore(text,pattern):
    if len(pattern) == 0:
        return []
    
    alphabet = set(text)
    last = LastOccur(pattern,alphabet)

    i = len(pattern) - 1 # Chỉ số của text
    j = len(pattern) - 1 # Chỉ số của pattern

    position = []

    while i < len(text):
        if text[i] == pattern[j]:
            if j == 0:
                position.append(i + 1)
                i += len(pattern)
                j = len(pattern) - 1
            else:
                i -= 1
                j -= 1
        else:
            l = last.get(text[i])
            i = i + len(pattern) - min(j, i + 1)
            j = len(pattern) - 1 # Sau khi dịch pattern thì ss lại từ cuối pattern
    return position

text = input()
pattern = input()

res = BoyerMoore(text, pattern)

if res:
    print(" ".join(map(str,res)))
else:
    print("-1")