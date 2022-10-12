if __name__ == '__main__':
    a = input()
    parentheses = 0
    curly_br = 0
    square_br = 0
    subsequence_start = 0
    subsequence_end = 0
    word = ''
    sup_word = ''
    sum = parentheses + curly_br + square_br
    sub_sum = sum
    def check(a):
        global parentheses, curly_br, square_br
        if a == '(':
            parentheses += 1
        elif a == '{':
            curly_br += 1
        elif a == '[':
            square_br += 1
        elif a == ')':
            parentheses -= 1
        elif a == '}':
            curly_br -= 1
        elif a == ']': 
            square_br -=1 
        
    if len(a) % 2 == 0 or a[0] != (')' or ']' or '}') or a[-1] != '(' or '[' or '{':
        for x in range(len(a)):
            if a[x] == ')' or a[x] == ']' or a[x] == '}':
                if (a[x-1] == '(' or a[x-1] =='[' or a[x-1] =='{') and ((a[x] != chr(ord(a[x-1]) + 2)) or (a[x] != chr(ord(a[x-1]) + 1))):
                    continue
            check(a[x])
            # print(parentheses + curly_br + square_br)
            word += a[x]
            print(word)
        if (parentheses + curly_br + square_br) == 0:
            print(True)
        else:
            print(False)
    else: print(False)
    