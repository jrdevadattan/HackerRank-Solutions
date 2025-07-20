def hurdleRace(k, height):
    a = max(height)
    if k > a:
        return 0
    else:
        return a - k

if __name__ == '__main__':
    first_multiple_input = input().rstrip().split()
    n = int(first_multiple_input[0])
    k = int(first_multiple_input[1])
    height = list(map(int, input().rstrip().split()))
    result = hurdleRace(k, height)
    print(result)
