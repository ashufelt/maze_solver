from tkinter import Tk, BOTH, Canvas
from window import Window
from basic_draw import Point, Line

def main():
    win = Window(800, 600)
    win.draw_line(Line(Point(20,20), Point(140,300)), "black")
    win.wait_for_close()

main()