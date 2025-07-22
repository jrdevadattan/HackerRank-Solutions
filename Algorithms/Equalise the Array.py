def equalizeArray(arr):
    a = 0
    for i in arr:
        if a < arr.count(i):
            a = arr.count(i)
    return len(arr) - a

if __name__ == '__main__':
    n = int(input().strip())
    arr = list(map(int, input().rstrip().split()))
    result = equalizeArray(arr)
    print(result)
