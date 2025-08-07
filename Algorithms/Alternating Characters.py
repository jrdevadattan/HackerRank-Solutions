def alternatingCharacters(s):
    d = 0
    for i in range(len(s)-1):
        if s[i] == s[i+1]:
            d += 1
    return d

if __name__ == '__main__':
    q = int(input())
    for _ in range(q):
        s = input()
        print(alternatingCharacters(s))
