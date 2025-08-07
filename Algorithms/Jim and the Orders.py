def jimOrders(o):
    a = []
    for i in range(len(o)):
        a.append((o[i][0] + o[i][1], i + 1))
    a.sort()
    return [x[1] for x in a]

if __name__ == '__main__':
    n = int(input())
    o = [list(map(int, input().split())) for _ in range(n)]
    print(*jimOrders(o))
