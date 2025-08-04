def howManyGames(p, d, m, s):
    c = 0
    while s >= p:
        s -= p
        c += 1
        p = max(p - d, m)
    return c
    
if __name__ == '__main__':
    first_multiple_input = input().rstrip().split()
    p = int(first_multiple_input[0])
    d = int(first_multiple_input[1])
    m = int(first_multiple_input[2])
    s = int(first_multiple_input[3])
    answer = howManyGames(p, d, m, s)
    print(answer)
