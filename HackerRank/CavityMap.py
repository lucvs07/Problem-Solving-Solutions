def cavityMap(grid, n):
    new_grid = grid
    print(new_grid)
    for row in range(1, n-1):
        new_row = list(grid[row])
        for col in range(1, n-1):
            curr_cell = grid[row][col]
            if (curr_cell > grid[row-1][col] and
                curr_cell > grid[row+1][col] and
                curr_cell > grid[row][col-1] and
                curr_cell > grid[row][col+1]):
                new_row[col] = 'X'
        new_grid[row] = ''.join(new_row)
    return new_grid
