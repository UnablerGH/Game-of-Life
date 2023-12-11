import numpy as np
from collections import defaultdict
import time
import matplotlib.pyplot as plt

def start_grid(size):
    return np.random.randint(2, size=(size, size))

def update_grid(grid):
    new_grid = np.zeros(grid.shape, dtype=int)
    for i in range(grid.shape[0]):
        for j in range(grid.shape[1]):
            new_grid[i][j] = int(update_cell(grid, i, j))
    return new_grid

def update_cell(grid, i, j):
    neighbors = get_neighbors(grid, i, j)
    if grid[i][j] == 1:
        if neighbors < 2:
            return 0
        elif neighbors > 3:
            return 0
        else:
            return 1
    else:
        if neighbors == 3:
            return 1
        else:
            return 0

def get_neighbors(grid, i, j):
    neighbors = 0
    for x in range(i-1, i+2):
        for y in range(j-1, j+2):
            if x == i and y == j:
                continue
            if x < 0 or y < 0 or x >= grid.shape[0] or y >= grid.shape[1]:
                continue
            if grid[x][y] == 1:
                neighbors += 1
    return neighbors

def show_grid(grid):
    plt.imshow(grid, cmap='gray')
    plt.pause(0.1) 

def main():
    size = 100
    start = start_grid(size)
    
    plt.ion() 
    
    for i in range(1000):
        if np.sum(start) == 0:
            break
        start = update_grid(start)
        show_grid(start)
        time.sleep(0.01)

    plt.ioff()  
    plt.show()  

main()
