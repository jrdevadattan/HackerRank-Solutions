def runningTime(arr):
    c = 0
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        while j >= 0 and arr[j] > key:
            arr[j+1] = arr[j]
            c += 1
            j -= 1
        arr[j+1] = key
    return c

if __name__ == '__main__':
    n = int(input().strip())
    arr = list(map(int, input().rstrip().split()))
    result = runningTime(arr)
    print(result)
