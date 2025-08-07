def surfaceArea(a):
    h, w = len(a), len(a[0])
    s = 0
    for i in range(h):
        for j in range(w):
            if a[i][j]:
                s += 2
            for x, y in [(0, 1), (1, 0), (0, -1), (-1, 0)]:
                ni, nj = i + x, j + y
                nh = a[ni][nj] if 0 <= ni < h and 0 <= nj < w else 0
                s += max(a[i][j] - nh, 0)
    return s

if __name__ == '__main__':
    first_multiple_input = input().rstrip().split()
    H = int(first_multiple_input[0])
    W = int(first_multiple_input[1])
    A = []
    for _ in range(H):
        A.append(list(map(int, input().rstrip().split())))
    result = surfaceArea(A)
    print(result)
