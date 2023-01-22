def sign_tree(seq: list, goal: int) -> list:  # возвращает порядок знаков или пустой список
    global signs
    if len(seq) == 1:  
        if seq[0] == goal: 
            return True
        else: return False
    for_plus = seq.copy()  # делает копию переданной последовательности
    for_minus = seq.copy()
    for_plus[1] = for_plus[0] + for_plus[1]  # складывает первые два элемента
    for_minus[1] = for_minus[0] - for_minus[1]  # вычитает первые два элемента
    if sign_tree(for_plus[1:], goal):
        signs += ['+']  # если выполнено условие, то добавляет '+' в список signs
        return signs
    if sign_tree(for_minus[1:], goal):
        signs += ['-']  # если выполнено условие, то добавляет '-' в список signs
        return signs

def output(seq: list, signs: list, goal: int) -> str:
    if not signs:  # если был передан пустой список, то возвращает 'no solution'
        return 'no solution'
    equation = f'{seq[0]} '
    for index in range(1, len(seq)):
        equation += f'{str(signs[index-1])} {str(seq[index])} '
    equation += f'= {goal}'
    return equation  # возвращает уравнение

if __name__ =='__main__':
    f = open('file.txt', 'r+')
    input_data = f.readline().split()
    N = int(input_data.pop(0))
    S = int(input_data.pop(-1))
    signs = []
    sequence = [int(x) for x in input_data]
    f.write('\n' + output(sequence, sign_tree(sequence, S), S))
    f.close()
    
