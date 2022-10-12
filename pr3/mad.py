with open('scob.txt', 'w') as file:
    a = ['(', ')']
    for x in range(2):
        for y in range(2):
            for z in range(2):
                for w in range(2):
                    for v in range(2):
                        for u in range(2):
                            file.write(a[x] + a[y] + a[z] + a[w] + a[v] + a[u])
                            file.write('\n')