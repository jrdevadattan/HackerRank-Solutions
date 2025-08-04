import math

def encryption(s):
    s = s.replace(' ', '')
    L = len(s)
    r = math.floor(math.sqrt(L))
    c = math.ceil(math.sqrt(L))
    if r * c < L:
        r += 1
    res = []
    for i in range(c):
        col_chars = []
        for j in range(i, L, c):
            col_chars.append(s[j])
        res.append(''.join(col_chars))
    return ' '.join(res)

if __name__ == '__main__':
    s = input()
    result = encryption(s)
    print(result)
