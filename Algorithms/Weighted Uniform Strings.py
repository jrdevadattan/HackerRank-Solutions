def weightedUniformStrings(s, queries):
    weights = set()
    prev = ''
    count = 0
    for ch in s:
        if ch == prev:
            count += 1
        else:
            count = 1
            prev = ch
        weights.add((ord(ch) - 96) * count)
    res = []
    for q in queries:
        res.append("Yes" if q in weights else "No")
    return res

if __name__ == '__main__':
    s = input()
    q_count = int(input())
    queries = [int(input()) for _ in range(q_count)]
    result = weightedUniformStrings(s, queries)
    print("\n".join(result))
