def absolutePermutation(n, k):
    if k == 0:
        return list(range(1, n + 1))
    if n % (2 * k) != 0:
        return [-1]
    res = []
    add = True
    for i in range(1, n + 1):
        res.append(i + k if add else i - k)
        if i % k == 0:
            add = not add
    return res
    
if __name__ == '__main__':
    t = int(input().strip())
    for t_itr in range(t):
        first_multiple_input = input().rstrip().split()
        n = int(first_multiple_input[0])
        k = int(first_multiple_input[1])
        result = absolutePermutation(n, k)
        for i in result:
            print(i, end=' ')
        print()
