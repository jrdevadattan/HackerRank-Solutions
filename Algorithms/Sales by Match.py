def sockMerchant(n, ar):
    a = 0
    d = {}
    for i in ar:
        d[i] = d.get(i,0) + 1
    for i in d.values():
        a += i//2
    return a
    
    
if __name__ == '__main__':
    n = int(input().strip())
    ar = list(map(int, input().rstrip().split()))
    result = sockMerchant(n, ar)
    print(result)
