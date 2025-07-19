def migratoryBirds(arr):
    d = {}
    for i in arr:
        d[i] = d.get(i, 0) + 1
    m = max(d.values())
    l = []
    for k, v in d.items():
        if v == m:
            l.append(k)
    return min(l)


if __name__ == '__main__':
    arr_count = int(input().strip())
    arr = list(map(int, input().rstrip().split()))
    result = migratoryBirds(arr)
    print(result)
