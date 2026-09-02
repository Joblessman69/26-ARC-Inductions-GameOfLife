#---------------------------- TASK 1 ----------------------------
def count_neighbors(grid, r, c):
    rows = len(grid)
    cols = len(grid[0])
    count = 0
    
    for dr in [-1, 0, 1]:
        for dc in [-1, 0, 1]:
            if dr == 0 and dc == 0:
                continue
            
            nr, nc = r + dr, c + dc
            
            if 0 <= nr < rows and 0 <= nc < cols:
                if grid[nr][nc] == 1:
                    count += 1
                    
    return count

#---------------------------- TASK 2 ----------------------------
def compute_next_generation(grid):
    rows = len(grid)
    cols = len(grid[0])
    
    new_grid = [[0 for _ in range(cols)] for _ in range(rows)]
    
    for r in range(rows):
        for c in range(cols):
            alive_neighbors = count_neighbors(grid, r, c)
            is_alive = grid[r][c] == 1
            
            if is_alive:
                if alive_neighbors == 2 or alive_neighbors == 3:
                    new_grid[r][c] = 1
                else:
                    new_grid[r][c] = 0
            else:
                if alive_neighbors == 3:
                    new_grid[r][c] = 1
                else:
                    new_grid[r][c] = 0
                    
    return new_grid