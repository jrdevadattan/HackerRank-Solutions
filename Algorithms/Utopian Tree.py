def utopianTree(n):
    c = 1
    for i in range(1, n+1):
        if i%2 == 0:
            c += 1
        else:
            c = c * 2
    return c

if __name__ == '__main__':
    t = int(input().strip())
    for t_itr in range(t):
        n = int(input().strip())
        result = utopianTree(n)
        print(result)
