from itertools import product
if __name__ == '__main__':
    numbers = {'1' : ['1', '2', '4'], 
                '2' : ['1', '2', '3', '5'], 
                '3' : ['3', '2', '6'], 
                '4' : ['1', '4' ,'5', '7'], 
                '5' : ['2', '4', '5', '6', '8'],
                '6' : ['3', '5', '6', '9'],
                '7' : ['4', '7', '8'],
                '8' : ['5', '7', '8', '9', '0'],
                '9' : ['6', '8', '9'],
                '0' : '8'} 
    sequence = input()
    var_numbers = []
    possible_passwords = []
    for num in sequence:
        var_numbers.append(numbers[num])
    for x in product(*var_numbers):
        possible_passwords.append(''.join(x))
    print(possible_passwords)
