def cutTheSticks(arr):
    l = []
    while True:
        if not arr:
            break
        l.append(len(arr))
        m = min(arr)
        for i in range(len(arr)):
            arr[i] -= m
        for j in range(arr.count(0)):
            arr.remove(0)
    return l

if __name__ == '__main__':
    n = int(input().strip())
    arr = list(map(int, input().rstrip().split()))
    result = cutTheSticks(arr)
    for i in result:
        print(i)
