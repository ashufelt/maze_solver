from cell import Cell
from window import Window
import time

class Maze():
    def __init__(self, x1, y1, num_rows, num_cols, cell_size_x, cell_size_y, win=None):
        self.__win = win
        self.__x1 = x1
        self.__y1 = y1
        self.__num_rows = num_rows
        self.__num_cols = num_cols
        self.__cell_size_x = cell_size_x if cell_size_x % 2 == 0 else cell_size_x + 1
        self.__cell_size_y = cell_size_y if cell_size_y % 2 == 0 else cell_size_y + 1
        self._cells = [[] for _ in range(num_cols)]
        self._create_cells()
    
    def _create_cells(self):
        current_cell_x = self.__x1
        for i in range(self.__num_cols):
            current_cell_y = self.__y1
            for j in range(self.__num_rows):
                self._cells[i].append(Cell(current_cell_x, current_cell_y, current_cell_x + self.__cell_size_x, current_cell_y + self.__cell_size_y, self.__win))
                current_cell_y += self.__cell_size_y
            current_cell_x += self.__cell_size_x
        for k in range(self.__num_rows):
            for l in range(self.__num_cols):
                self._draw_cell(l, k)
        self._break_entrance_and_exit()
    
    def _draw_cell(self, i, j):
        self._cells[i][j].draw()
        self._animate()
    
    def _animate(self):
        if self.__win is None:
            return
        self.__win.redraw()
        time.sleep(0.02)
    
    def _break_entrance_and_exit(self):
        top_left_cell = self._cells[0][0]
        top_left_cell.has_top_wall = False
        top_left_cell.draw()

        bottom_right_cell = self._cells[self.__num_cols-1][self.__num_rows-1]
        bottom_right_cell.has_bottom_wall = False
        bottom_right_cell.draw()

        