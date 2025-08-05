def workbook(n, k, arr):
    p = 1
    s = 0
    for i in arr:
        for j in range(1, i + 1):
            if j == p:
                s += 1
            if j % k == 0 or j == i:
                p += 1
    return s

if __name__ == '__main__':
    first_multiple_input = input().rstrip().split()
    n = int(first_multiple_input[0])
    k = int(first_multiple_input[1])
    arr = list(map(int, input().rstrip().split()))
    result = workbook(n, k, arr)
    print(result)
