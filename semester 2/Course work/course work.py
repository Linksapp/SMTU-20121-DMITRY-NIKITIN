import sys
import customtkinter as ctk
import pygame
from time import time
pygame.init()

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
LIGHTPINK = (255, 182, 193)
SILVER = (192,192,192)
DIMGREY = (105,105,105)
FPS = 60


class Board:
    def __init__(self, board_size: int):
        self.board_size = board_size
        self.width = int(500 / self.board_size)
        self.height = int(500 / self.board_size)
        self.margin = 5
        self.board_grid = [self.board_size * [0] for x in range(self.board_size)]

    def fill_board_grid(self, surface, grid, size):
        for row in range(size):
                for column in range(size):
                    self.color = WHITE
                    if grid[row][column] == '#':
                        self.color = RED
                    if grid[row][column] == '*':
                        self.color = LIGHTPINK
                    pygame.draw.rect(surface,
                             self.color,
                             [(self.margin + self.width) * column + self.margin,
                              (self.margin + self.height) * row + self.margin,
                              self.width,
                              self.height])

    def attacked_cell(self, x: int, y: int, board_size: int) -> list:
        self.attacked = []
        for num in range(1, 3):
            if (x - num) >= 0 and (y - num) >= 0:
                self.attacked.append((x - num, y - num))
            if (x + num) < board_size and (y - num) >= 0:
                self.attacked.append((x + num, y - num))
            if (x - num) >= 0 and (y + num) < board_size:
                self.attacked.append((x - num, y + num))
            if (x + num) < board_size and (y + num) < board_size:
                self.attacked.append((x + num, y + num))
        return self.attacked
    
class Figure:
    ...

class Input_window(ctk.CTk):
    def __init__(self, x=700, y=500) -> None:
        super().__init__()
        self.num_size_check = (self.register(self._do_size_validation), '%P')
        self.num_figures_check = (self.register(self._do_figures_validation), '%P')
        self.board_size_label = ctk.CTkLabel(self, text='Размер доски: ')
        self.board_size_entry = ctk.CTkEntry(self, validate='key', validatecommand=self.num_size_check, border_width=0)
        self.number_of_figures_label = ctk.CTkLabel(self, text='Количество фигур: ')
        self.number_of_figures_entry = ctk.CTkEntry(self, validate='key', validatecommand=self.num_figures_check, border_width=0)
        self.get_button = ctk.CTkButton(self, text='Next>>', command=self._create_pygame_window)
        self.board_size_label.grid(row=0, column=0)
        self.board_size_entry.grid(row=0, column=1)
        self.number_of_figures_label.grid(row=1, column=0)
        self.number_of_figures_entry.grid(row=1, column=1)
        self.get_button.grid(row=2, column=3)

    def _create_pygame_window(self) -> None:
        if self.board_size_entry.get() != '' and self.number_of_figures_entry.get() != '':
            board_window = Pygame_board_window(int(self.board_size_entry.get()), int(self.number_of_figures_entry.get()))
            self.destroy()
            board_window.make_board()
        

    def _do_size_validation(self, new_value: str) -> bool:
        if new_value.isnumeric():
            return len(new_value) <= 2 and (int(new_value) <= 20) and new_value[0] != '0'
        else: return new_value == ''
    def _do_figures_validation(self, new_value: str) -> bool:
        if new_value.isnumeric():
            return len(new_value) <= 2 and new_value != '00'
        else: return new_value == '' 


class Pygame_button:
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def make_button(self, text, text_size=26):
        self.font = pygame.font.SysFont('timesnewroman', text_size)
        button = self.font.render(text, True, BLACK, SILVER)
        return button
    
    def get_clicked(self, action=None, *args):
        action(*args)

class Pygame_window:
    def __init__(self, board_size: int, number_of_figures: int):
        self.board_size = board_size
        self.number_of_figures = number_of_figures
        self.width = int(500 / self.board_size)
        self.height = int(500 / self.board_size)
        self.margin = 5
        self.run = True
        self.clock = pygame.time.Clock()
        self.side = int((self.width + self.margin) * self.board_size + self.margin)
        self.window_size = [self.side, self.side+50]
        self.scr = pygame.display.set_mode(self.window_size)
        self.board_surface = pygame.Surface((self.side, self.side))
        self.button_surface = pygame.Surface((self.side, 50))
        self.continue_button = Pygame_button(95, 30)
        self.board_maker = Board(self.board_size)
        self.board_grid = self.board_maker.board_grid

    def blit_objects(self, text: str, grid):
        self.scr.blit(self.board_surface, (0, 0))
        self.scr.blit(self.button_surface, (0, self.side))
        self.board_maker.fill_board_grid(self.board_surface, grid, self.board_size)
        self.button_surface.blit(self.continue_button.make_button(text), (self.side-100, 10))
    
    @staticmethod
    def no_solution_window():
        scr = pygame.display.set_mode([500, 500])
        scr.fill(WHITE)
        font = pygame.font.SysFont('timesnewroman', 80)
        no_solution = font.render('No solution', True, BLACK, SILVER)
        scr.blit(no_solution, (60, 200))
        output.write('no solutions')
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    quit()  
                elif event.type == pygame.MOUSEBUTTONDOWN:
                    quit()
            pygame.display.update()       

class Pygame_output_window(Pygame_window):
    def __init__(self, board_size, number_of_figures, coords):
        super().__init__(board_size, number_of_figures)
        self.coords = coords
        self.xstart = 0
        self.ystart = 0
        self.firstboard = None
        self.solution(self.xstart, self.ystart, 
                                        self.putting_given_figure([self.board_size * [0] for x in range(self.board_size)], self.board_size, self.coords),
                                         self.number_of_figures, self.coords, True)
        print(self.firstboard)
        if self.firstboard is not None:
            self.putting_given_figure([self.board_size * [0] for x in range(self.board_size)], self.board_size, self.firstboard)
        else:
            self.no_solution_window()

    def display_first_solution(self):
        while self.run:
            self.blit_objects('Записать', self.putting_given_figure([self.board_size * [0] for x in range(self.board_size)], self.board_size, self.firstboard))
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    quit()
                    
                elif event.type == pygame.MOUSEBUTTONDOWN:
                    self.pos = pygame.mouse.get_pos()
                    if self.pos[0] in range(self.side-100, self.side-5) and self.pos[1] in range(self.side, self.side+40): 
                        self.atime = time()
                        self.solution(self.xstart, self.ystart, self.putting_given_figure(self.board_grid, self.board_size, self.coords), 
                                      self.number_of_figures, self.coords, False)
                        
                        self.btime = time() - self.atime
                        output.seek(0) # воозвращаемся к началу файла, это необходимо, что бы len(output.readlines()) вывелось количество элементов
                        print(f'Количество решений: {len(output.readlines())}')
                        for _ in self.putting_given_figure(self.board_grid, self.board_size ,self.firstboard): print(*_)
                        print(f'Время работы {self.btime}')
                        sys.exit()

                            


            self.clock.tick(FPS)
            pygame.display.update()
    
    def solution(self, xstart: int, ystart: int, board: list, fig_num: int, standing: list, first: bool) -> None:
        if fig_num == 0:
            if standing == []: return None
            if first:
                self.firstboard = standing
                return

            for _ in [*standing]: output.write(str(_) + ' ') # распаковываем standing и каждый элемент переводим в строку
            output.write('\n')
        else: 
            for x in range(xstart, len(board)): # xstart нужен, чтобы мы не проходились по уже пройденным клеткам
                for y in range(len(board)):
                    # print(x)
                    if x == xstart and y < ystart:  # эта проверка служит для того же
                        continue
                    if board[x][y] == 0 and self.under_attack(x, y, board):  # проверка является ли клетка 0 и находится ли она под ударом
                        board[x][y] = '#' # ставим фигуру
                        # if first and fig_num == 0:
                        #     return standing + [tuple([x, y])]
                        self.solution(x, y, board, fig_num - 1, standing + [tuple([x, y])], first)
                        '''передаём координаты, оставшееся количество фигур, 
                        которые надо поставить и уже стоящие фигуры'''
                        board[x][y] = 0  # убираем фигуру

    def under_attack(self, x: int, y: int, board: list) -> bool: 
        '''проверяем находится ли клетка под ударом, если находится возвращаем False '''
        for num in range(1, 3):
            if (x - num) >= 0 and (y - num) >= 0 and board[x - num][y - num] == '#':
                return False
            if (x + num) < len(board) and (y - num) >= 0 and board[x + num][y - num] == '#':
                return False
            if (x - num) >= 0 and (y + num) < len(board) and board[x - num][y + num] == '#':
                return False
            if (x + num) < len(board) and (y + num) < len(board) and board[x + num][y + num] == '#':
                return False
        return True

    def putting_given_figure(self, board, size: int, coordinates: list) -> list:
        '''Расставляет заданные фигуры'''
        for x, y in coordinates:
            board[x][y] = '#' # ставит фигуру
            for cell in self.board_maker.attacked_cell(x, y, size):
                board[cell[0]][cell[1]] = '*'   # показывает атакуемую клетку
        return board


class Pygame_board_window(Pygame_window):
    def __init__(self, board_size: int, number_of_figures: int):
        super().__init__(board_size, number_of_figures)
        self.coords = []
        self.all_attacked = {}

    def _create_output_window(self, size, number_of_figures, coords):
        self.run = False
        self.output_window = Pygame_output_window(size, number_of_figures, coords)
        self.output_window.display_first_solution()
        

    def make_board(self) -> None:
        pygame.display.set_caption('Board')
        self.icon = pygame.image.load('semester 2\Course work\chess_icon.png')
        pygame.display.set_icon(self.icon)
        
        while self.run:
            self.blit_objects('Continue', self.board_grid)
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    print(self.coords)
                    quit()
                    
                elif event.type == pygame.MOUSEBUTTONDOWN:
                    self.pos = pygame.mouse.get_pos()
                    self.column = self.pos[0] // (self.width + self.margin)
                    self.row = self.pos[1] // (self.height + self.margin)
                    if self.pos[0] in range(self.side-100, self.side-5) and self.pos[1] in range(self.side+5, self.side+40): 
                        self.continue_button.get_clicked(self._create_output_window, self.board_size, self.number_of_figures, self.coords)
                    if (self.row >= self.board_size or self.column >= self.board_size): continue
                    self.attacked = self.board_maker.attacked_cell(self.row, self.column, self.board_size)

                    if event.dict['button'] == 1:
                        
                        if not((self.row >= self.board_size or self.column >= self.board_size)):
                            if self.board_grid[self.row][self.column] == '#' or self.board_grid[self.row][self.column] == '*' or self.number_of_figures == 0:
                                continue
                            
                            for cell in self.attacked:
                                self.board_grid[cell[0]][cell[1]] = '*'
                                if self.all_attacked.get(cell) == None:
                                    self.all_attacked[cell] = 1
                                else: self.all_attacked[cell] +=1

                            self.coords.append((self.row, self.column))
                            self.board_grid[self.row][self.column] = '#'
                            self.number_of_figures -= 1

                    elif event.dict['button'] == 3:
                        if self.board_grid[self.row][self.column] == '#':
                            for cell in self.attacked:
                                self.all_attacked[cell] -= 1
                                if self.all_attacked[cell] == 0: 
                                    self.board_grid[cell[0]][cell[1]] = 0
                                    del self.all_attacked[cell]

                        if self.board_grid[self.row][self.column] == '#':
                            del self.coords[self.coords.index((self.row, self.column))]
                            self.board_grid[self.row][self.column] = 0
                            self.number_of_figures +=1

            self.clock.tick(FPS)
            pygame.display.update()

if __name__ == '__main__':
    output = open('semester 2\Course work\output.txt', 'w+')
    app = Input_window()

    app.mainloop()
    output.close()
    
    
    # N, L, K = file[0].split()
    # standing_figure = [tuple([int(file[x].split()[0]), int(file[x].split()[1])]) for x in range(1, int(K) + 1)]
