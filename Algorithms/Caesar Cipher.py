def caesarCipher(s, k):
    k %= 26
    res = []
    for ch in s:
        o = ord(ch)
        if 'a' <= ch <= 'z':
            res.append(chr((o - 97 + k) % 26 + 97))
        elif 'A' <= ch <= 'Z':
            res.append(chr((o - 65 + k) % 26 + 65))
        else:
            res.append(ch)
    return ''.join(res)

if __name__ == '__main__':
    n = int(input().strip())
    s = input()
    k = int(input().strip())
    print(caesarCipher(s, k))
