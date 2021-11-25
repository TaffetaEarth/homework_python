def sudoku_validator(grid, i, j, e):
    counter = 0
    for x in range(9):
        if e != grid[i][x]:
            counter += 1
    if counter == 9:
        counter = 0
        for x in range(9):
            if e != grid[x][j]:
                counter += 1
        if counter == 9:
            top_x, top_y = 3 * (i // 3), 3 * (j // 3)  # for left top coords
            for x in range(top_x, top_x + 3):
                for y in range(top_y, top_y + 3):
                    if grid[x][y] == e:
                        return False
            return True
    return False


def empty_cell_founder(grid, i, j):
    for x in range(i, 9):
        for y in range(j, 9):
            if grid[x][y] == 0:
                return x, y
    for x in range(0, 9):
        for y in range(0, 9):
            if grid[x][y] == 0:
                return x, y
    return -1, -1


def sudoku_solver(grid, i=0, j=0):
    i, j = empty_cell_founder(grid, i, j)
    if i == -1:
        return True
    for e in range(1, 10):
        if sudoku_validator(grid, i, j, e):
            grid[i][j] = e
            if sudoku_solver(grid, i, j):
                return True
            grid[i][j] = 0
    return False


sudoku = [[5, 1, 7, 6, 0, 0, 0, 3, 4], [2, 8, 9, 0, 0, 4, 0, 0, 0], [3, 4, 6, 2, 0, 5, 0, 9, 0],
          [6, 0, 2, 0, 0, 0, 0, 1, 0], [0, 3, 8, 0, 0, 6, 0, 4, 7], [0, 0, 0, 0, 0, 0, 0, 0, 0],
          [0, 9, 0, 0, 0, 0, 0, 7, 8], [7, 0, 3, 4, 0, 0, 5, 6, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0]]
sudoku_solver(sudoku)
print(sudoku)
