def theLoveLetterMystery(s):
    c = 0
    i, j = 0, len(s) - 1
    while i < j:
        c += abs(ord(s[i]) - ord(s[j]))
        i += 1
        j -= 1
    return c

if __name__ == '__main__':
    q = int(input())
    for _ in range(q):
        s = input()
        print(theLoveLetterMystery(s))
