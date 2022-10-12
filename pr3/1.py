if __name__ == '__main__':
    a = input()
    new_a = ''
    max = ''
    for x in range(len(a)):
        if a[x] in new_a:
            new_a = ''
        new_a += a[x]
        if len(new_a) > len(max): max = new_a
    print(max) 