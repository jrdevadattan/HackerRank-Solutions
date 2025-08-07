def gemstones(arr):
    common = set(arr[0])
    for rock in arr[1:]:
        common &= set(rock)
    return len(common)

if __name__ == '__main__':
    n = int(input().strip())
    arr = [input() for _ in range(n)]
    print(gemstones(arr))
