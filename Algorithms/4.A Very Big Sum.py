def aVeryBigSum(ar):
    long = sum(ar)
    return long

n = int(input())
l = list(map(int, input().strip().split()))
r = aVeryBigSum(l)
print(r)
