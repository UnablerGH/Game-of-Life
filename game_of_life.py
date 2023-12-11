import numpy as np
import time
import matplotlib.pyplot as plt

def start_grid(size):
    return np.random.randint(2, size=(size, size), dtype=int)

def update_grid(grid):
    neighbor_count = (
        np.roll(grid, shift=(1, 1), axis=(0, 1)) + np.roll(grid, shift=1, axis=0) +
        np.roll(grid, shift=(1, -1), axis=(0, 1)) + np.roll(grid, shift=-1, axis=0) +
        np.roll(grid, shift=(1, 0), axis=(0, 1)) + np.roll(grid, shift=-1, axis=1) +
        np.roll(grid, shift=(0, 1), axis=(0, 1)) + np.roll(grid, shift=1, axis=1)
    )

    new_grid = ((grid == 1) & ((neighbor_count == 2) | (neighbor_count == 3))) | ((grid == 0) & (neighbor_count == 3))
    return new_grid.astype(int)

def show_grid(grid):
    plt.imshow(grid, cmap='gray')
    plt.pause(0.01)

def main():
    size = 30
    start = start_grid(size)
    
    plt.ion()
    
    for _ in range(1000):
        if np.sum(start) == 0:
            break
        start = update_grid(start)
        show_grid(start)
        time.sleep(0.01)

    plt.ioff()
    plt.show()

main()
