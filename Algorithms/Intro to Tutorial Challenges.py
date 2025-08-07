def introTutorial(V, arr):
    for i in range(len(arr)):
        if arr[i] == V:
            return i

if __name__ == '__main__':
    V = int(input().strip())
    n = int(input().strip())
    arr = list(map(int, input().rstrip().split()))
    result = introTutorial(V, arr)
    print(result)
