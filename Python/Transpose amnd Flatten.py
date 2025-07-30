import numpy
l = []
n, m = map(int, input().strip().split())
for i in range(n):
    ar = l.append(list(map(int, input().strip().split())))
myarray = numpy.array(l)
print(numpy.transpose(myarray))
print(myarray.flatten())
