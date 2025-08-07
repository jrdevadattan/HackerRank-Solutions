def missingNumbers(a, b):
    d = {}
    for x in b:
        d[x] = d.get(x, 0) + 1
    for x in a:
        d[x] -= 1
    r = []
    for k in d:
        if d[k] > 0:
            r.append(k)
    return sorted(r)

if __name__ == '__main__':
    n = int(input())
    a = list(map(int, input().split()))
    m = int(input())
    b = list(map(int, input().split()))
    print(*missingNumbers(a, b))
