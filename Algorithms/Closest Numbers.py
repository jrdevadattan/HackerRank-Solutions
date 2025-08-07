def closestNumbers(a):
    a.sort()
    d = float('inf')
    r = []
    for i in range(1, len(a)):
        x = a[i] - a[i-1]
        if x < d:
            d = x
            r = [a[i-1], a[i]]
        elif x == d:
            r += [a[i-1], a[i]]
    return r

if __name__ == '__main__':
    n = int(input().strip())
    arr = list(map(int, input().rstrip().split()))
    res = closestNumbers(arr)
    print(*res)
