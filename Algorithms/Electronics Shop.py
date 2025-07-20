def getMoneySpent(keyboards, drives, b):
    s = 0
    for i in keyboards:
        for j in drives:
            if s < i + j <= b:
                s = i+j
    if s == 0:
        return -1
    else:
        return s     

if __name__ == '__main__':
    bnm = input().split()
    b = int(bnm[0])
    n = int(bnm[1])
    m = int(bnm[2])
    keyboards = list(map(int, input().rstrip().split()))
    drives = list(map(int, input().rstrip().split()))
    moneySpent = getMoneySpent(keyboards, drives, b)
    print(moneySpent)
