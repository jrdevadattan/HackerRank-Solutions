def circularArrayRotation(a, k, queries):
    for i in range(k):
        x = a.pop()
        a.insert(0,x)
    for i in queries:
        print(a[i])
    
if __name__ == '__main__':
    first_multiple_input = input().rstrip().split()
    n = int(first_multiple_input[0])
    k = int(first_multiple_input[1])
    q = int(first_multiple_input[2])
    a = list(map(int, input().rstrip().split()))
    queries = []
    for _ in range(q):
        queries_item = int(input().strip())
        queries.append(queries_item)
    result = circularArrayRotation(a, k, queries)
