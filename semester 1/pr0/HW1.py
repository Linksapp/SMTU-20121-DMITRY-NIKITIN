from xml.dom.pulldom import parseString


if __name__ == '__main__':
    a, c = [int(input()), int(input()), int(input())], 0
    for x in a:
        if x % 2 == 0:
            c+=1
    print(c)    
    for x in range(10, 2, 2):print(1)
    a   = 'bbaaa'
    print(min(a))