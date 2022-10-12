if __name__ == '__main__':
    a, b = input(), int(input())
    word = ''
    brg = 2*(b - 1)
    if 1 < b < 3:
        print(a)
    elif b < 0:
        print()
    else:
        for x in range(b):
            number = x
            if x == 0 or x == b - 1:
                while number < len(a):
                    word += a[number]
                    number += brg
            else:
                j = brg - x
                while j < len(a) or number < len(a):
                    word += a[number]
                    if j < len(a):
                        word += a[j]
                    number += brg
                    j += brg
    print(word)
    