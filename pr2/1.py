if __name__ == '__main__':
    a = input()
    new_a = ''
    max = ''
    for x in range(len(a)):
        for y in range(x, len(a)):
            if a[y] in new_a:
                new_a = ''
                break
            new_a += a[y]
            if len(new_a) > len(max): max = new_a
    print(max)