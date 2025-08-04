from collections import Counter

x = int(input())
s = Counter(map(int, input().split()))
n = int(input())
t = 0
for _ in range(n):
    sz, p = map(int, input().split())
    if s[sz]:
        t += p
        s[sz] -= 1
print(t)
