from itertools import permutations

s, r = input().split()
r = int(r)
s = ''.join(sorted(s))

for p in permutations(s, r):
    print(''.join(p))
