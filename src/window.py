import tkinter as tk
from basic_draw import Line


class Window():
    def __init__(self, height, width):
        self.__height = height
        self.__width = width
        self.__root = tk.Tk()
        self.__root.title('Maze Solver')
        self.canvas = tk.Canvas(height=self.__height, width=self.__width)
        self.canvas.pack()
        self.__running = False
        self.__root.protocol("WM_DELETE_WINDOW", self.close)
    
    def redraw(self):
        self.__root.update_idletasks()
        self.__root.update()
    
    def wait_for_close(self):
        self.__running = True
        while self.__running:
            self.redraw()

    def close(self):
        self.__running = False
    
    def draw_line(self, line, fill_color):
        line.draw(self.canvas, fill_color)
        