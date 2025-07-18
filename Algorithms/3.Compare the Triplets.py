def compareTriplets(a,b):
    l = [0,0]
    for i in range(3):
        if a[i] > b[i]:
            l[0] += 1
        elif a[i] < b[i]:
            l[1] += 1
        else:
            pass
    return l

a = map(int, input().strip().split())
b = map(int, input().strip().split())
r = compareTriplets(list(a), list(b))
for i in r:
    print(i, end=" ")
