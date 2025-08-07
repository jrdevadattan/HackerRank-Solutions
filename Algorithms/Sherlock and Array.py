def balancedSums(a):
    s = sum(a)
    l = 0
    for x in a:
        s -= x
        if l == s:
            return "YES"
        l += x
    return "NO"

if __name__ == '__main__':
    for _ in range(int(input())):
        input()
        arr = list(map(int, input().split()))
        print(balancedSums(arr))
