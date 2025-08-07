def countingSort(arr):
    c = [0]*100
    for x in arr:
        c[x] += 1
    res = []
    for i in range(100):
        res.extend([i]*c[i])
    return res

if __name__ == '__main__':
    n = int(input())
    arr = list(map(int, input().split()))
    result = countingSort(arr)
    print(*result)
