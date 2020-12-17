#!/usr/bin/env python3

from os import path

def main():

    grid = []
    for _ in range(13):
        z_grid = []
        for _ in range(13):        
            x_grid = []
            for _ in range(20):
                y_grid = []
                for _ in range(20):                
                    y_grid.append('.')
                x_grid.append(y_grid)
            z_grid.append(x_grid)
        grid.append(z_grid)

    z_initial = grid[6][6]
    x_idx = 6
    y_idx = 6
    for line in get_input():
        for char in line:
            z_initial[x_idx][y_idx] = char
            y_idx += 1
        x_idx += 1
        y_idx = 6

    for cycle in range(6):
        print(f'Running cycle #{cycle+1}')
        grid = apply_cycle(grid)

    active_count = 0
    for w_grid in grid:
        for z_grid in w_grid:
            for x_grid in z_grid:
                for cell in x_grid:
                    if cell == '#':
                        active_count += 1  
    
    print(f'Active cells after 6 cycles: {active_count}')

def apply_cycle(grid):
    new_grid = []
    for idx_w, w_grid in enumerate(grid):
        new_z_grid = []
        for idx_z, z_grid in enumerate(w_grid):
            new_x_grid = []
            for idx_x, x_grid in enumerate(z_grid):
                new_y_grid = []
                for idx_y, _ in enumerate(x_grid):
                    new_y_grid.append(get_new_cube_status(idx_w, idx_z, idx_x, idx_y, grid))
                new_x_grid.append(new_y_grid)
            new_z_grid.append(new_x_grid)
        new_grid.append(new_z_grid)
    return new_grid

def get_new_cube_status(idx_w, idx_z, idx_x, idx_y, grid):
    current_state = grid[idx_w][idx_z][idx_x][idx_y]
    active_neighbors = 0
    for w in range(idx_w - 1, idx_w + 2):
        if w < 0 or w >= len(grid):
            continue
        for z in range(idx_z - 1, idx_z + 2):
            if z < 0 or z >= len(grid[w]):
                continue
            for x in range(idx_x - 1, idx_x + 2):
                if x < 0 or x >= len(grid[w][z]):
                    continue
                for y in range(idx_y - 1, idx_y + 2):
                    if y < 0 or y >= len(grid[w][z][x]):
                        continue
                    if w == idx_w and z == idx_z and x == idx_x and y == idx_y:
                        continue
                    if grid[w][z][x][y] == '#':
                        active_neighbors += 1
    if current_state == '#':
        if 1 < active_neighbors < 4:
            return '#'
        else:
            return '.'
    else:
        if active_neighbors == 3:
            return '#'
        else:
            return '.'
    
def get_input():
    with open(path.join(path.dirname(__file__), 'input')) as f:
        return [i.strip() for i in f.readlines()]

if __name__ == '__main__':
    main()
