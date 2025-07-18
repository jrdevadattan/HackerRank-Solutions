def diagonalDifference(ar):
    c = len(ar[0])
    lr = 0
    rl = 0
    for i in range(c):
        lr += ar[i][i]
        rl += ar[i][(c-1)-i] 
    d = abs(lr-rl) 
    return d
   
l = [] 
n = int(input())
for i in range(n):
    b = list(map(int, input().strip().split()))
    l.append(b)
r = diagonalDifference(l)
print(r)
