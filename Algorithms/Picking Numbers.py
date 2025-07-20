def pickingNumbers(a):
    c = 0
    for i in a:
        b = a.count(i) + a.count(i+1)
        if c < b:
            c = b
    return c
         
if __name__ == '__main__':
    n = int(input().strip())
    a = list(map(int, input().rstrip().split()))
    result = pickingNumbers(a)
    print(result)
