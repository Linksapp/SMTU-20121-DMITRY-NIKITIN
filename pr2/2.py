if __name__ == '__main__':
    a = input().split()
    if len(a) > 1:
        a.reverse()
    a = ' '.join(a)
    a = a.capitalize()
    print(a)    