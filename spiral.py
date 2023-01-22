if __name__ == '__main__':
    size = int(input())
    matrix = [size * [0] for x in range(size)]
    num = 1
    i, j = 0, 0
    while num != size*size + 1: 
        while j < size and matrix[i][j] == 0:
                matrix[i][j] = num
                j += 1
                num += 1
        j -= 1
        i += 1
        while i < size and matrix[i][j] == 0:
            matrix[i][j] = num
            i +=1
            num += 1
        i -= 1
        j -= 1
        while j >= 0 and matrix[i][j] == 0:
            matrix[i][j] = num
            j -=1
            num += 1
            
        j += 1
        i -= 1
        while i >= 0 and matrix[i][j] == 0:
            matrix[i][j] = num
            i -= 1
            num += 1
        i += 1
        j += 1


        
    for x in matrix:
        print(x)
