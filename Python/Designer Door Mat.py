n, m = map(int, input().split())

for i in range(n):
    if i == n // 2:
        w = 'WELCOME'
        p = w.center(m, '-')
        print(p)
    else:
        if i < n // 2:
            x = 2 * i + 1
        else:
            x = 2 * (n - i - 1) + 1
        s = '.|.' * x
        p = s.center(m, '-')
        print(p)
