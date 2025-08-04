from itertools import combinations

s, r = input().split()
r = int(r)
s = ''.join(sorted(s))

for i in range(1, r+1):
    for comb in combinations(s, i):
        print(''.join(comb))
