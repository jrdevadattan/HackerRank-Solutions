def stones(n, a, b):
    s = set()
    for i in range(n):
        s.add((n-i-1)*a + i*b)
    return sorted(s)
    
if __name__ == '__main__':
    T = int(input().strip())
    for T_itr in range(T):
        n = int(input().strip())
        a = int(input().strip())
        b = int(input().strip())
        result = stones(n, a, b)
        for i in result:
            print(i, end=' ')
        print()
