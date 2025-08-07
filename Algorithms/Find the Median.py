def findMedian(a):
    a.sort()
    return a[len(a)//2]

if __name__ == '__main__':
    n = int(input().strip())
    arr = list(map(int, input().rstrip().split()))
    print(findMedian(arr))
