def simpleArraySum(ar):
    s=0
    for i in ar:
        s += int(i)
    return s

n = int(input())
num = input()
l = num.strip().split()
r = simpleArraySum(l)
print(r)
