def saveThePrisoner(n, m, s):
    a = m + (s - 1)
    b = a % n
    if b == 0:
        return n
    else:
        return b
        
if __name__ == '__main__':
    t = int(input().strip())
    for t_itr in range(t):
        first_multiple_input = input().rstrip().split()
        n = int(first_multiple_input[0])
        m = int(first_multiple_input[1])
        s = int(first_multiple_input[2])
        result = saveThePrisoner(n, m, s)
        print(result)
