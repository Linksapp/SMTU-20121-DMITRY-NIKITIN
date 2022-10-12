if __name__ == '__main__':
    a = int(input())
    if -2**7 <= a <= 2**7 - 1:
        if a % 10 == 0:
            a //= 10
        if a > 0:
            a = str(a)[::-1]
        elif a < 0:
            a = str(a)[1::]
            a = '-' + a[::-1]

        if -2**7 <= int(a) <= 2**7 - 1: print(a)
        else: print('no solution')
    else: print('no solution')