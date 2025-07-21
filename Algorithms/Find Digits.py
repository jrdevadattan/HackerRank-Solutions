def findDigits(n):
    c = 0
    l = list(str(n))
    for i in l:
        if int(i) != 0:
            if n % int(i) == 0:
                c += 1
    return c

if __name__ == '__main__':
    t = int(input().strip())
    for t_itr in range(t):
        n = int(input().strip())
        result = findDigits(n)
        print(result)
