def kangaroo(x1, v1, x2, v2):
    while True:
        if x1 == x2:
            print("YES")
            break
        if x1 > x2 or v2 > v1:
            print("NO")
            break
        x1 += v1
        x2 += v2

if __name__ == '__main__':
    first_multiple_input = input().rstrip().split()
    x1 = int(first_multiple_input[0])
    v1 = int(first_multiple_input[1])
    x2 = int(first_multiple_input[2])
    v2 = int(first_multiple_input[3])
    result = kangaroo(x1, v1, x2, v2)
