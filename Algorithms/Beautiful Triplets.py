def beautifulTriplets(d, arr):
    s = set(arr)
    c = 0
    for x in arr:
        if x + d in s and x + 2*d in s:
            c += 1
    return c

if __name__ == '__main__':
    first_multiple_input = input().rstrip().split()
    n = int(first_multiple_input[0])
    d = int(first_multiple_input[1])
    arr = list(map(int, input().rstrip().split()))
    result = beautifulTriplets(d, arr)
    print(result)
