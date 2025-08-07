def countSort(arr):
    n = len(arr)
    max_val = 0
    for x, _ in arr:
        val = int(x)
        if val > max_val:
            max_val = val
    buckets = [[] for _ in range(max_val+1)]
    half = n // 2
    for i, (x, s) in enumerate(arr):
        val = int(x)
        if i < half:
            buckets[val].append('-')
        else:
            buckets[val].append(s)
    res = []
    for b in buckets:
        res.extend(b)
    print(*res)

if __name__ == '__main__':
    n = int(input().strip())
    arr = []
    for _ in range(n):
        arr.append(input().rstrip().split())
    countSort(arr)
