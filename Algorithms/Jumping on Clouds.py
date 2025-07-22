def jumpingOnClouds(c):
    j = 0
    i = 0
    n = len(c)
    while i < (n - 1):
        if i + 2 < n and c[i + 2] == 0:
            i += 2
        else:
            i += 1
        j += 1
    return j
            
if __name__ == '__main__':
    n = int(input().strip())
    c = list(map(int, input().rstrip().split()))
    result = jumpingOnClouds(c)
    print(result)
