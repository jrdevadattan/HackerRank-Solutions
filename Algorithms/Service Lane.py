def serviceLane(n, cases):
    res = []
    for c in cases:
        start, end = c[0], c[1]
        res.append(min(width[start:end+1]))
    return res

if __name__ == '__main__':
    first_multiple_input = input().rstrip().split()
    n = int(first_multiple_input[0])
    t = int(first_multiple_input[1])
    width = list(map(int, input().rstrip().split()))
    cases = []
    for _ in range(t):
        cases.append(list(map(int, input().rstrip().split())))
    result = serviceLane(n, cases)
    for i in result:
        print(i)
