def countingSort(arr):
    freq = [0] * 100
    for num in arr:
        freq[num] += 1
    return freq

if __name__ == '__main__':
    n = int(input().strip())
    arr = list(map(int, input().rstrip().split()))
    result = countingSort(arr)
    print(" ".join(map(str, result)))
