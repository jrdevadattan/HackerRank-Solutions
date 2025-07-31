def organizingContainers(container):
    l = len(container)
    x = [sum([container[i][j] for j in range(l)]) for i in range(l)]
    y = [sum([container[i][j] for i in range(l)]) for j in range(l)]
    if sorted(x) == sorted(y):
        return "Possible"
    else:
        return "Impossible"
        
if __name__ == '__main__':
    q = int(input().strip())
    for q_itr in range(q):
        n = int(input().strip())
        container = []
        for _ in range(n):
            container.append(list(map(int, input().rstrip().split())))
        result = organizingContainers(container)
        print(result)
