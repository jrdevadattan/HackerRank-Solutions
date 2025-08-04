def print_rangoli(n):
    a = [chr(97 + i) for i in range(n)]
    w = 4 * n - 3
    p = []
    for i in range(n):
        l = a[n-1:i:-1] + a[i:n]
        s = '-'.join(l).center(w, '-')
        p.append(s)
    for i in range(n-1, 0, -1):
        print(p[i])
    for i in range(n):
        print(p[i])

if __name__ == '__main__':
    n = int(input())
    print_rangoli(n)
