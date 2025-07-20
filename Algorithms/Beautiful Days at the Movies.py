def beautifulDays(i, j, k):
    c = 0
    for x in range(i, j+1):
        a = int(str(x)[::-1])
        b = abs(a-x)
        if b%k == 0:
            c += 1
    return c
            

if __name__ == '__main__':
    first_multiple_input = input().rstrip().split()
    i = int(first_multiple_input[0])
    j = int(first_multiple_input[1])
    k = int(first_multiple_input[2])
    result = beautifulDays(i, j, k)
    print(result)
