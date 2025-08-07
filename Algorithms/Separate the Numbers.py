def separateNumbers(s):
    l = len(s)
    for i in range(1, l//2 + 1):
        f = s[:i]
        if f[0] == '0':
            continue
        n = int(f)
        b = f
        while len(b) < l:
            n += 1
            b += str(n)
        if b == s:
            print("YES", f)
            return
    print("NO")

if __name__ == '__main__':
    q = int(input().strip())
    for _ in range(q):
        s = input()
        separateNumbers(s)
