from collections import namedtuple
bank = namedtuple('bank', 'bank_name amount_of_money')
if __name__ == '__main__':
    banks_count = int(input())
    banks_list = []
    for _ in range(banks_count):
        banks_list.append(bank(input('Имя банка: '), int(input('Количество миллионов в сейфе: '))))
        
