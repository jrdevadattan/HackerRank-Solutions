if __name__ == '__main__':
    s = input()
    d = {}
    for ch in s:
        d[ch] = d.get(ch, 0) + 1

    l = list(d.items())
    l.sort(key=lambda x: (-x[1], x[0]))

    for i in range(3):
        print(l[i][0], l[i][1])
