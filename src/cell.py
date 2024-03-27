from window import Window
from basic_draw import Point, Line

class Cell():
    def __init__(self, x1, y1, x2, y2, window=None, wall_color="black"):
        self.has_left_wall = True
        self.has_right_wall = True
        self.has_top_wall = True
        self.has_bottom_wall = True
        self.__x1 = x1
        self.__y1 = y1
        self.__x2 = x2
        self.__y2 = y2
        self.__center = Point((x1+x2)//2, (y1+y2)//2)
        self.__win = window
        self.__wall_color = wall_color
        self.visited = False
    
    def draw(self):
        if self.__win is None:
            return
        self.__win.draw_line(Line(Point(self.__x1, self.__y1), Point(self.__x2, self.__y1)), self.__wall_color if self.has_top_wall else "#d9d9d9")
        self.__win.draw_line(Line(Point(self.__x1, self.__y2), Point(self.__x2, self.__y2)), self.__wall_color if self.has_bottom_wall else "#d9d9d9")
        self.__win.draw_line(Line(Point(self.__x1, self.__y1), Point(self.__x1, self.__y2)), self.__wall_color if self.has_left_wall else "#d9d9d9")
        self.__win.draw_line(Line(Point(self.__x2, self.__y1), Point(self.__x2, self.__y2)), self.__wall_color if self.has_right_wall else "#d9d9d9")
    
    def draw_move(self, to_cell, undo=False):
        if self.__win is None:
            return
        self.__win.draw_line(Line(self.__center, to_cell.__center), "gray" if undo else "red")