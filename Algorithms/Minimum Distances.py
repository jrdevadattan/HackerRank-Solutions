def minimumDistances(a):
    t = {}
    m = -1
    for i in range(len(a)):
        if a[i] in t:
            d = i - t[a[i]]
            if m == -1 or d < m:
                m = d
            t[a[i]] = i
        else:
            t[a[i]] = i
    return m

if __name__ == '__main__':
    n = int(input().strip())
    a = list(map(int, input().rstrip().split()))
    result = minimumDistances(a)
    print(result)
