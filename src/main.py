from tkinter import Tk, BOTH, Canvas
from window import Window
from basic_draw import Point, Line
from cell import Cell
from maze import Maze

def main():
    win = Window(820, 620)
    maze = Maze(10, 10, 16, 12, 50, 50, win)
    win.wait_for_close()
    

main()