if __name__ == '__main__':
    n = []
    for i in range(int(input())):
        name = input()
        score = float(input())
        n.append([name,score])
    s = [j[1] for j in n]
    sc = sorted(set(s))
    for k in sorted(n):
        if k[1] == sc[1]:
            print(k[0])
