def pageCount(n, p):
    start = p//2
    if n%2 == 0:
        n = n + 1
    stop = (n-p)//2
    return min(start, stop)

if __name__ == '__main__':
    n = int(input().strip())
    p = int(input().strip())
    result = pageCount(n, p)
    print(result)
