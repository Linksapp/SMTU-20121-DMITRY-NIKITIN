alph_list = input().split()
new_alph_list = []
buffer = []
second_buffer = []
position = 0
while len(alph_list) != 0:
    new_alph_list.append([alph_list[0]])
    for x in range(1, len(alph_list)):
        buffer.extend(alph_list[0])
        buffer.sort()
        second_buffer.extend(alph_list[x])
        second_buffer.sort()
        if buffer == second_buffer:
            new_alph_list[position].append(alph_list[x])
        buffer, second_buffer = [], []
    for j in new_alph_list[position]:
        alph_list.remove(j)
    position += 1
print(new_alph_list)
