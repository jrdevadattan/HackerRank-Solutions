def viralAdvertising(n):
    s = 5
    c = 0
    for i in range(n):
        l = s//2
        s = l*3
        c += l
    return c
        

if __name__ == '__main__':
    n = int(input().strip())
    result = viralAdvertising(n)
    print(result)
