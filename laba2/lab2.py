from copy import deepcopy

def main():
    input_data = open('laba2/input_data.txt')
    file = list(input_data)
    N, L, K = file[0].split()
    standing_figure = [tuple([int(file[x].split()[0]), int(file[x].split()[1])]) for x in range(1, int(K) + 1)]
    count = 0
    b = chess(putting_given_figure(int(N), standing_figure), int(L))
    print(b)
    for x in b:
        print(x)
        # break
        count += 1
    print(count)

def figure_searcher(board):
    figures = []
    for x in range(len(board)):
        for y in range(len(board)):
            if board[x][y] == '#':
                figures.append((x, y))
    return figures

def chess(board, L):
    variants = []
    if L == 0:
        return figure_searcher(board)
    for x in range(len(board)):
        for y in range(len(board)):
            if board[x][y] == 0:
                variants.append((chess(put_figure(x, y, deepcopy(board)), L - 1)))
    return variants
                
def put_figure(x, y, board_p):
    board_p[x][y] = '#'
    for cell in attacked_cell(x, y, len(board_p)):
        board_p[cell[0]][cell[1]] = '*'
    return board_p

def attacked_cell(x: int, y: int, size: int) -> list:
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
    board = [size * [0] for x in range(size)]
    for x, y in coordinates:
        board[x][y] = '#'
        for cell in attacked_cell(x, y, size):
            board[cell[0]][cell[1]] = '*'
    return board

if __name__ == '__main__':
    main()
