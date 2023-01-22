def num_tree(seq: list, goal: int) -> list: 
    global signs
    if len(seq) == 1:
        if seq[0] == goal:
            return True
        else: return False
    for_plus = seq.copy()
    for_minus = seq.copy()
    for_plus[0] = for_plus[0] + for_plus[1]
    for_plus.pop(1)
    for_minus[0] = for_minus[0] - for_minus[1]
    for_minus.pop(1)
    if num_tree(for_plus, goal):
        signs += ['+']
        return signs
    if num_tree(for_minus, goal):
        signs += ['-']
        return signs

def output(seq: list, signs: list, goal: int) -> str:
    if not signs:
        return 'no solution'
    equation = f'{seq[0]}'
    for index in range(1, len(seq)):
        equation += ' ' + str(signs[index-1]) + ' ' + str(seq[index])
    equation += f' = {goal}'
    return equation

if __name__ =='__main__':
    input_data = input().split()
    N = int(input_data.pop(0))
    S = int(input_data.pop(-1))
    signs = []
    sequence = [int(x) for x in input_data]
    print(output(sequence, num_tree(sequence, S), S))
    
