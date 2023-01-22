from collections import namedtuple
bank = namedtuple('bank', 'bank_name amount_of_money')
if __name__ == '__main__':
    banks_count = int(input())
    banks_list = []
    indexes = []
    for _ in range(banks_count):
        banks_list.append(bank(input('Имя банка: '), int(input('Количество миллионов в сейфе: ')))) # input('Имя банка: ')
    banks_money = [0 for x in range(len(banks_list))]
    if banks_list[0].amount_of_money >= banks_list[1].amount_of_money:
        banks_money[0], banks_money[1] = banks_list[0].amount_of_money, banks_list[0].amount_of_money
        indexes.extend([[0], [0]])
    else:
        banks_money[0], banks_money[1] = banks_list[0].amount_of_money, banks_list[1].amount_of_money
        indexes.extend([[0], [1]])
    
    if len(banks_list) >= 3:
        for bank in range(2, len(banks_list)):
            if banks_money[bank-1] >= banks_money[bank-2] + banks_list[bank].amount_of_money:
                banks_money[bank] = banks_money[bank-1]
                indexes.append(indexes[bank-1])
            else:
                banks_money[bank] = banks_money[bank-2] + banks_list[bank].amount_of_money
                indexes.append(indexes[bank-2] + [bank])
    else:
        print(max(banks_money))
    final = [max(banks_money)]
    print(banks_money.index(max(banks_money)))
    for _ in indexes[banks_money.index(max(banks_money))]:
        final.append((banks_list[_].bank_name, _+1))
    print(final)