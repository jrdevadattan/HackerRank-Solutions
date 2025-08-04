def queensAttack(n, k, r_q, c_q, obstacles):
    o = set((r, c) for r, c in obstacles)
    d = [
        (1, 0), (-1, 0),
        (0, 1), (0, -1),
        (1, 1), (-1, -1),
        (1, -1), (-1, 1)
    ]
    c = 0
    for dr, dc in d:
        r, c_ = r_q, c_q
        while 1 <= r + dr <= n and 1 <= c_ + dc <= n:
            r += dr
            c_ += dc
            if (r, c_) in o:
                break
            c += 1
    return c
    
if __name__ == '__main__':
    n, k = map(int, input().split())
    r, c = map(int, input().split())
    obs = [list(map(int, input().split())) for _ in range(k)]
    print(queensAttack(n, k, r, c, obs))
