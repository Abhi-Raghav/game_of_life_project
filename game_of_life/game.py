import numpy as np
import os
import time
from rich.console import Console
os.system('cls' if os.name == 'nt' else 'clear')

class CoreGameEngine:
    def __init__(self, grid_size=(20, 20)):
        self.__grid_size = np.array(grid_size, dtype=int)
        self.__current_grid = np.random.randint(2, size=grid_size)

        #self.__current_grid = np.zeros(self.__grid_size)
        #self.__current_grid[10][10] = 1
        #self.__current_grid[10][11] = 1
        #self.__current_grid[10][12] = 1


        self.__iter = 0

    def __update_cell(self, row, col):

        # The rules of Game of life:
        # The universe of the Game of Life is an infinite, two-dimensional orthogonal grid of square cells,
        # each of which is in one of two possible states, live or dead, (or populated and unpopulated, respectively).
        # Every cell interacts with its eight neighbours, which are the cells that are horizontally, vertically,
        # or diagonally adjacent. At each step in time, the following transitions occur:
        #
        # Any live cell with fewer than two live neighbours dies, as if by underpopulation.
        # Any live cell with two or three live neighbours lives on to the next generation.
        # Any live cell with more than three live neighbours dies, as if by overpopulation.
        # Any dead cell with exactly three live neighbours becomes a live cell, as if by reproduction.

        max_row, max_col = np.shape(self.__current_grid)
        if row == max_row - 1 or row == 0 or col == max_col - 1 or col == 0:
            return 0
        else:
            value_sum_neighbours = self.__current_grid[row+1][col-1] + self.__current_grid[row+1][col] + \
                                   self.__current_grid[row+1][col+1] + self.__current_grid[row][col-1] + \
                                   self.__current_grid[row][col+1] + self.__current_grid[row-1][col-1] + \
                                   self.__current_grid[row-1][col] + self.__current_grid[row-1][col+1]

            if self.__current_grid[row][col] == 1:  # alive

                if value_sum_neighbours < 2:
                    return 0
                elif value_sum_neighbours < 4:
                    return 1
                else:
                    return 0
            else:   # dead

                if value_sum_neighbours == 3:
                    return 1
                else:
                    return 0

    def update_grid(self):
        new_grid = self.__current_grid.copy()
        max_row, max_col = np.shape(new_grid)
        for i in range(max_row):
            for j in range(max_col):
                new_grid[i][j] = self.__update_cell(i, j)
        self.__current_grid = new_grid

    def print_grid(self):
        os.system('cls' if os.name == 'nt' else 'clear')
        console = Console()
        time.sleep(0.5)
        for row in self.__current_grid:
            for col in row:
                if col == 1:  # alive
                    console.print(":white_large_square:", end=" ")
                else:   # dead
                    # console.print(" ", end=" ")
                    console.print(":black_large_square:", end=" ")
            console.print()

    def animate(self, no_of_frames=500):
        pass


if __name__ == "__main__":
    new_game = CoreGameEngine()
    for frames in range(0, 10000):
        new_game.print_grid()
        new_game.update_grid()
        print()









