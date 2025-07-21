def extraLongFactorials(n):
    c = 1
    for i in range(1, n+1):
        c = c * i
    return c
        
if __name__ == '__main__':
    n = int(input().strip())
    r = extraLongFactorials(n)
    print(r)
