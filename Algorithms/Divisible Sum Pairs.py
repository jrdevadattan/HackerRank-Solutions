def divisibleSumPairs(n, k, ar):
    a = sorted(ar)
    c = 0
    for i in range(n):
        for j in range(i+1, n):
            s = a[i] + a[j]
            if s % k == 0:
                c += 1
    return c

if __name__ == '__main__':
    first_multiple_input = input().rstrip().split()
    n = int(first_multiple_input[0])
    k = int(first_multiple_input[1])
    ar = list(map(int, input().rstrip().split()))
    result = divisibleSumPairs(n, k, ar)
    print(result)
