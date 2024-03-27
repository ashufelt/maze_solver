from tkinter import Tk, BOTH, Canvas
from window import Window
from basic_draw import Point, Line
from cell import Cell
from maze import Maze

def main():
    win = Window(820, 620)
    maze = Maze(10, 10, 16, 12, 50, 50, win)
    '''
    cell1 = Cell(20, 20, 40, 40, win)
    cell1.has_top_wall = False
    cell1.draw()

    cell2 = Cell(50, 20, 70, 40, win)
    cell2.has_bottom_wall = False
    cell2.draw()

    cell3 = Cell(20, 50, 40, 70, win)
    cell3.has_right_wall = False
    cell3.draw()

    cell4 = Cell(50, 50, 70, 70, win)
    cell4.has_left_wall = False
    cell4.draw()
    '''
    win.wait_for_close()
    

main()