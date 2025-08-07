def quickSort(arr):
    p = arr[0]
    left = [x for x in arr if x < p]
    equal = [x for x in arr if x == p]
    right = [x for x in arr if x > p]
    return left + equal + right

if __name__ == '__main__':
    n = int(input().strip())
    arr = list(map(int, input().rstrip().split()))
    result = quickSort(arr)
    print(" ".join(map(str, result)))
