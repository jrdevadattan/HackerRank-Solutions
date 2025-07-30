import numpy

n, m, p = map(int, input().strip().split())
l = []
k = []
for i in range(n):
    l.append(list(map(int, input().strip().split())))
for i in range(m):
    k.append(list(map(int, input().strip().split())))

array_1 = numpy.array(l)
array_2 = numpy.array(k)
print(numpy.concatenate((array_1, array_2), axis=0))
