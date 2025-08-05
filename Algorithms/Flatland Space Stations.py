def flatlandSpaceStations(n, c):
    c.sort()
    res = c[0]
    for i in range(1, len(c)):
        d = (c[i] - c[i - 1]) // 2
        res = max(res, d)
    res = max(res, n - 1 - c[-1])
    return res

if __name__ == '__main__':
    nm = input().split()
    n = int(nm[0])
    m = int(nm[1])
    c = list(map(int, input().rstrip().split()))
    result = flatlandSpaceStations(n, c)
    print(result)
