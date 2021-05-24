import numpy as np


class CoreGameEngine:
    def __init__(self, grid_size=[500, 500]):
        self.__grid_size = np.array(grid_size, dtype=int)
        self.__current_grid = np.zeros(self.__grid_size)
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
        if row == max_row or col == max_col:
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
        row, col = np.shape(new_grid)
        for i in row:
            for j in col:
                new_grid[i][j] = self.__update_cell(row, col)









