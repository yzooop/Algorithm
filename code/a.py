import sys

input = sys.stdin.read

def print_grid(grid):
    for row in grid:
        print("".join(row))

def plant_bombs(grid, R, C):
    return [['O'] * C for _ in range(R)]

def explode_bombs(grid, R, C):
    new_grid = [['O'] * C for _ in range(R)]
    for r in range(R):
        for c in range(C):
            if grid[r][c] == 'O':
                new_grid[r][c] = '.'
                if r > 0:
                    new_grid[r - 1][c] = '.'
                if r < R - 1:
                    new_grid[r + 1][c] = '.'
                if c > 0:
                    new_grid[r][c - 1] = '.'
                if c < C - 1:
                    new_grid[r][c + 1] = '.'
    return new_grid

def solve_bomberman(R, C, N, initial_grid):
    if N == 1:
        return initial_grid

    if N % 2 == 0:
        return plant_bombs(initial_grid, R, C)

    grid_after_3_sec = explode_bombs(initial_grid, R, C)
    grid_after_5_sec = explode_bombs(grid_after_3_sec, R, C)

    if N % 4 == 1:
        return grid_after_5_sec
    else:
        return grid_after_3_sec

data = input().strip().split()
R, C, N = int(data[0]), int(data[1]), int(data[2])
initial_grid = [list(data[i + 3]) for i in range(R)]

result_grid = solve_bomberman(R, C, N, initial_grid)
print_grid(result_grid)
