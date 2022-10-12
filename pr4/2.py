N = input()
n = len(N)
new_N = []
fact_N = 1
while n > 1:
    fact_N *= n
    n -=1 
N_list = []
position = 0
for x in range(fact_N):
    for j in range(fact_N // number):
        new_N.append([])
        new_N.append[position](N[x%4])
        position += 1
    number = len(N)
    