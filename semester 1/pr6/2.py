def roman_numerals(number):
    roman_base = {'I' : 1, 'V' : 5, 'X' : 10, 'L' : 50, 'C' : 100, 'D' : 500, 'M' : 1000}
    arabic_num = roman_base[number[-1]]
    for num in range(2, len(number)+1):
        if number[-num] == 'I':
            if number[-(num-1)] == 'X' or number[-(num-1)] == 'V':
                arabic_num -= 1
            else:
                arabic_num += 1
        if number[-num] == 'X':
            if number[-(num-1)] == 'L' or number[-(num-1)] == 'C':
                arabic_num -= 10
            else:
                arabic_num += 10
        if number[-num] == 'C':
            if number[-(num-1)] == 'D' or number[-(num-1)] =='M':
                arabic_num -= 100
            else:
                arabic_num += 100
        if number[-num] == 'V':
            arabic_num += 5
        if number[-num] == 'L':
            arabic_num += 50
        if number[-num] == 'D':
            arabic_num += 500
        if number[-num] == 'M':
            arabic_num += 1000
    return arabic_num
if __name__ == '__main__':
    print(roman_numerals(input().upper()))
    