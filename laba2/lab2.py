from time import time

def main():
    atime = time()  # время начала работы функции chess
    chess(0, 0, putting_given_figure(int(N), standing_figure), int(L), standing_figure)
    btime = time() - atime  # время окончания работы функции chess
    output.seek(0)  # воозвращаемся к началу файла, чтобы read() считала содержимое с начала файла
    if output.read() != '': # проверка на отсутствие решений
        output.seek(0) # воозвращаемся к началу файла, это необходимо, что бы len(output.readlines()) вывелось количество элементов
        print(f'Количество решений: {len(output.readlines())}')
        for _ in putting_given_figure(int(N), standing_figure + firstboard): print(*_)
        print(f'Время работы {btime}')
    else: print('no solution'), output.write('no solution')
    
def chess(xstart: int, ystart: int, board: list, fig_num: int, standing: list) -> None:
    global firstboard   

    if fig_num == 0:
        if firstboard is None: firstboard = standing
        for _ in [*standing]: output.write(str(_) + ' ') # распаковываем standing и каждый элемент переводим в строку
        output.write('\n')
    else: 
        for x in range(xstart, len(board)): # xstart нужен, чтобы мы не проходились по уже пройденным клеткам
            for y in range(len(board)):
                if x == xstart and y < ystart:  # эта проверка служит для того же
                    continue
                if board[x][y] == 0 and under_attack(x, y, board):  # проверка является ли клетка 0 и находится ли она под ударом
                    board[x][y] = '#' # ставим фигуру
                    chess(x, y, board, fig_num - 1, standing + [tuple([x, y])])
                    '''передаём координаты, оставшееся количество фигур, 
                       которые надо поставить и уже стоящие фигуры'''
                    board[x][y] = 0  # убираем фигуру
 

def under_attack(x: int, y: int, board: list) -> bool: 
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

def attacked_cell(x: int, y: int, size: int) -> list:
    '''Делает то же самое, что и так under_attack, но возвращает список, 
    чтобы можно было передать в функцию putting_given_figure'''
    attacked = []
    for num in range(1, 3):
        if (x - num) >= 0 and (y - num) >= 0:
            attacked.append((x - num, y - num))
        if (x + num) < size and (y - num) >= 0:
            attacked.append((x + num, y - num))
        if (x - num) >= 0 and (y + num) < size:
            attacked.append((x - num, y + num))
        if (x + num) < size and (y + num) < size:
            attacked.append((x + num, y + num))
    return attacked

def putting_given_figure(size: int, coordinates: list) -> list:
    '''Расставляет заданные фигуры'''
    board = [int(N) * [0] for x in range(int(N))]   # создаёт матрицу N * N нулей
    for x, y in coordinates:
        board[x][y] = '#' # ставит фигуру
        for cell in attacked_cell(x, y, size):
            board[cell[0]][cell[1]] = '*'   # показывает атакуемую клетку
    return board


if __name__ == '__main__':
    input_data = open('laba2/input.txt')
    output = open('laba2/output.txt', 'w+')
    file = list(input_data)
    firstboard = None
    N, L, K = file[0].split()
    standing_figure = [tuple([int(file[x].split()[0]), int(file[x].split()[1])]) for x in range(1, int(K) + 1)]
    main()
    
