from cell import Cell
from window import Window
import time
import random

class Maze():
    def __init__(self, x1, y1, num_rows, num_cols, cell_size_x, cell_size_y, win=None, seed=None):
        self.__win = win
        self.__x1 = x1
        self.__y1 = y1
        self.__num_rows = num_rows
        self.__num_cols = num_cols
        self.__cell_size_x = cell_size_x if cell_size_x % 2 == 0 else cell_size_x + 1
        self.__cell_size_y = cell_size_y if cell_size_y % 2 == 0 else cell_size_y + 1
        self._cells = [[] for _ in range(num_cols)]
        self._create_cells()
        if seed is not None:
            random.seed(seed)
        self._break_walls_r(0, 0)
        self._reset_cells_visited()
    
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
    
    def _animate(self, t=0.02):
        if self.__win is None:
            return
        self.__win.redraw()
        time.sleep(t)
    
    def _break_entrance_and_exit(self):
        top_left_cell = self._cells[0][0]
        top_left_cell.has_top_wall = False
        top_left_cell.draw()

        bottom_right_cell = self._cells[self.__num_cols-1][self.__num_rows-1]
        bottom_right_cell.has_bottom_wall = False
        bottom_right_cell.draw()
    
    def _break_walls_r(self, i, j):
        self._cells[i][j].visited = True
        # print(f"Setting cell at {i}, {j} to visited = True")
        while True:
            directions = []
            if i > 0:
                if self._cells[i-1][j].visited is False:
                    directions.append((-1, 0))
            if j > 0:
                if self._cells[i][j-1].visited is False:
                    directions.append((0, -1))
            if i < self.__num_cols-1:
                if self._cells[i+1][j].visited is False:
                    directions.append((1, 0))
            if j < self.__num_rows-1:
                if self._cells[i][j+1].visited is False:
                    directions.append((0, 1))
            # print(f"valid directions from cell {i}, {j} = {directions}")
            if len(directions) == 0:
                self._cells[i][j].draw()
                self._animate(0.05)
                return
            chosen_dir = random.choice(directions)
            self._break_between_two_cells(i, j, chosen_dir)
            self._break_walls_r(i + chosen_dir[0], j + chosen_dir[1])
        
    def _break_between_two_cells(self, i, j, chosen_dir):
        if chosen_dir[0] == 1:
            self._cells[i][j].has_right_wall = False
            self._cells[i+1][j].has_left_wall = False
            # print(f"Moving right from {i},{j}")
            # print(f"Removing right wall from {i},{j}")
            # print(f"Removing left wall from {i+1},{j}")
        elif chosen_dir[0] == -1:
            self._cells[i][j].has_left_wall = False
            self._cells[i-1][j].has_right_wall = False
            # print(f"Moving left from {i},{j}")
            # print(f"Removing left wall from {i},{j}")
            # print(f"Removing right wall from {i-1},{j}")
        elif chosen_dir[1] == 1:
            self._cells[i][j].has_bottom_wall = False
            self._cells[i][j+1].has_top_wall = False
            # print(f"Moving down from {i},{j}")
            # print(f"Removing bottom wall from {i},{j}")
            # print(f"Removing top wall from {i},{j+1}")
        elif chosen_dir[1] == -1:
            self._cells[i][j].has_top_wall = False
            self._cells[i][j-1].has_bottom_wall = False
            # print(f"Moving up from {i},{j}")
            # print(f"Removing top wall from {i},{j}")
            # print(f"Removing bottom wall from {i},{j-1}")
    
    def _reset_cells_visited(self):
        for i in range(self.__num_cols):
            for j in range(self.__num_rows):
                self._cells[i][j].visited = False

    def solve(self):
        return self._solve_r()
    
    def _solve_r(self):
        self._animate(0.5)
        return True