def permutationEquation(p):
    l = []
    for i in range(1, len(p)+1):
        a = p.index(i) + 1
        b = p.index(a) + 1
        l.append(b)
    return l

if __name__ == '__main__':
    n = int(input().strip())
    p = list(map(int, input().rstrip().split()))
    result = permutationEquation(p)
    for i in result:
        print(i)
