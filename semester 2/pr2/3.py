import tkinter as tk
from abc import ABC, abstractmethod

class Figure(ABC):
    @abstractmethod
    def draw_figure(self):
        ...
        

    @abstractmethod
    def get_figure_area(self):
        ...

        

class MainWindow(tk.Tk):
    def __init__(self):
        super().__init__()

        self.label = tk.Label(self, text='Выберете нужную фигуру:').grid(row=0, sticky='SNWE')
        self.circle_button = tk.Button(self, text='Круг', command=self.circule_window).grid(row=1, sticky='WE')
        self.square_button = tk.Button(self, text='Квадрат', command=self.square_window).grid(row=2, sticky='WE')
        self.rectangle_button = tk.Button(self, text='Прямоугольник', command=self.rectangle_window).grid(row=3, sticky='WE')

        self.mainloop()

    def circule_window(self):
        self.circle = Input_window('Круг')
    
    def square_window(self):
        self.circle = Input_window('Квадрат')

    def rectangle_window(self):
        self.rect = Input_window('Прямоугольник')

class Circle(tk.Toplevel, Figure):
    def __init__(self, radius):
        super().__init__()
        self.radius = radius

    def draw_figure(self):
        c = tk.Canvas(self)
        c.create_oval(5, 5, 50+2*self.radius, 50+2*self.radius, width=2)
        self.button = tk.Button(self, text='Узнать площадь фигуры', command=self.get_figure_area).pack()
        c.pack()

    def get_figure_area(self):
        self.window = tk.Toplevel(self)
        self.label = tk.Label(self.window, text=f'Площадь фигуры - {3.14*(self.radius**2)}').grid(row=0)
        self.button = tk.Button(self.window, text='OK', command=exit).grid(row=1)

class Square(tk.Toplevel, Figure):
    def __init__(self, side):
        super().__init__()
        self.side = side

    def draw_figure(self):
        c = tk.Canvas(self)
        c.create_rectangle(5, 5, 50+self.side, 50+self.side)
        self.button = tk.Button(self, text='Узнать площадь фигуры', command=self.get_figure_area).pack()
        c.pack()

    def get_figure_area(self):
        self.window = tk.Toplevel(self)
        self.label = tk.Label(self.window, text=f'Площадь фигуры - {self.side**2}').grid(row=0)    
        self.button = tk.Button(self.window, text='OK', command=exit).grid(row=1)

class Rectangle(tk.Toplevel, Figure):
    def __init__(self, x, y):
        super().__init__()
        self.x = x
        self.y = y


    def draw_figure(self):
        canvas = tk.Canvas(self)
        canvas.create_rectangle(5, 5, 50+self.x, 50+self.y)
        self.button = tk.Button(self, text='Узнать площадь фигуры', command=self.get_figure_area).pack()
        canvas.pack()
    
    def get_figure_area(self):
        self.window = tk.Toplevel(self)
        self.label = tk.Label(self.window, text=f'Площадь фигуры - {self.x * self.y}').grid(row=0)    
        self.button = tk.Button(self.window, text='OK', command=exit).grid(row=1)

class Input_window(tk.Toplevel):
    def __init__(self, fig):
        super().__init__()
        self.fig = fig
        if fig == 'Круг':
            self.text = 'Введите радиус круга:'
            self.command = self.make_circle
        elif fig == 'Квадрат':
            self.text = 'Введите сторону квадрата:'
            self.command = self.make_square
        elif fig == 'Прямоугольник':
            self.text = 'Введите стороны прямоугольника:'
            self.command = self.make_rect

        
        self.label = tk.Label(self, text=self.text).grid(row=0)
        self.entry = tk.Entry(self)
        self.entry.grid(row=1, sticky='WE')
        self.button = tk.Button(self, text='Продолжить', command=self.command).grid(row=2)

    def make_circle(self):
        self.rad = int(self.entry.get())
        if self.rad > 0:
            fig = Circle(self.rad)
            fig.draw_figure()
            

    def make_square(self):
        self.side = int(self.entry.get())
        if self.side > 0:
            fig = Square(self.side)
            fig.draw_figure()

    def make_rect(self):
        self.sides = self.entry.get().split()
        if int(self.sides[0]) > 0 and int(self.sides[1]) > 0:
            fig = Rectangle(int(self.sides[0]), int(self.sides[1]))
            fig.draw_figure()

app = MainWindow()