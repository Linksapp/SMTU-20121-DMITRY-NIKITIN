if __name__ == '__main__':
    N = input().split()
    n = len(N)
    new_N = []
    temp = []
    buffer = []
    if n == 1:
        new_N.append(int(N[0]))
    else:
        if new_N == []:
            new_N.append([[0 for i in range(n)]])
        for y in N:
            for n_list in new_N:
                for un_n_list in n_list:
                    for x in range(len(un_n_list)):  
                        if un_n_list[x] == 0:
                            temp = un_n_list.copy()            
                            temp[x] = int(y)
                            if temp not in buffer:
                                buffer.append(temp)
            new_N.append(buffer)
            buffer = []
            del new_N[0]
        new_N = new_N[0]
    print(new_N)
    
