def minimumNumber(n, p):
    nums = "0123456789"
    low = "abcdefghijklmnopqrstuvwxyz"
    up = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    spec = "!@#$%^&*()-+"
    c1 = c2 = c3 = c4 = 0
    for x in p:
        if x in nums:
            c1 = 1
        elif x in low:
            c2 = 1
        elif x in up:
            c3 = 1
        elif x in spec:
            c4 = 1
    miss = 4 - (c1 + c2 + c3 + c4)
    return max(miss, 6 - n)

if __name__ == '__main__':
    n = int(input().strip())
    p = input()
    print(minimumNumber(n, p))
