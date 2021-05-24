import numpy as np


class CoreGameEngine:
    def __init__(self, grid_size=[500, 500]):
        self.__grid_size = np.array(grid_size, dtype=int)
        self.__current_grid = np.zeros(self.__grid_size)
        self.__future_grid = self.__current_grid.copy()
        self.__iter = 0

    def update_cell(self, row, col):
        max_row, max_col = np.shape(self.__current_grid)
        if row == max_row or col == max_col:
            pass

    def update_grid(self):
        pass






