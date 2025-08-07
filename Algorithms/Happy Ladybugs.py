def happyLadybugs(b):
    if '_' not in b:
        for i in range(len(b)):
            if (i > 0 and b[i] == b[i-1]) or (i < len(b)-1 and b[i] == b[i+1]):
                continue
            return "NO"
        return "YES"
    d = {}
    for c in b:
        if c != '_':
            d[c] = d.get(c, 0) + 1
    for v in d.values():
        if v == 1:
            return "NO"
    return "YES"

if __name__ == '__main__':
    g = int(input().strip())
    for g_itr in range(g):
        n = int(input().strip())
        b = input()
        result = happyLadybugs(b)
        print(result)
