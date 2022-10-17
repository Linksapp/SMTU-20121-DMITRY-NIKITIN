if __name__ == '__main__':
    a, b, c = [int(x) for x in input().split()]
    if a == b == c:
        print(3)
    elif a == b or b == c or a == c:
        print(2)
    else:
        print(0)
