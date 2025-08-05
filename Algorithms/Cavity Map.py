def cavityMap(grid):
    n = len(grid)
    output = grid[:]
    grid = [list(row) for row in grid]
    for i in range(1, n - 1):
        for j in range(1, n - 1):
            cell = grid[i][j]
            if (cell > grid[i-1][j] and
                cell > grid[i+1][j] and
                cell > grid[i][j-1] and
                cell > grid[i][j+1]):
                output[i] = output[i][:j] + 'X' + output[i][j+1:]
    return output
  

if __name__ == '__main__':
    n = int(input().strip())
    grid = []
    for _ in range(n):
        grid_item = input()
        grid.append(grid_item)
    result = cavityMap(grid)
    for i in result:
        print(i)
    
