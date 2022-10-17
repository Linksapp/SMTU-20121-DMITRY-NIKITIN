from collections import namedtuple
students = (namedtuple('stud_list', 'name age mark hometown'))
def good_students():
    students_list = [students('Dmitry', '18', '4.38', 'MOSCOW'), students('Alexander', '17', '3.78', 'MOSCOW'), students('Michael', '19', '4.89', 'MOSCOW'), students('Alex', '18', '4.67', 'MOSCOW'), students('Yaroslav', '21', '4.93', 'MOSCOW'), students('Nikita', '19', '3.78', 'MOSCOW'), students('Gregory', '19', '2.56', 'MOSCOW')]
    mark_sum = 0
    for x in students_list:
        mark_sum += float(x.mark)
    mark_sum /= len(students_list)
    good_students_list = []
    for x in students_list:
        if float(x.mark) > mark_sum:
            good_students_list.append(x.name)
    print('Ученики {0} в этом семестре хорошо учатся!'.format(good_students_list))
good_students()