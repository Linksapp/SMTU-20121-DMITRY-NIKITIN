from collections import namedtuple
a = namedtuple('A', 'name age group')
b = a('Dima', 12, 3)
print(b)