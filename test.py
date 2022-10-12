class Mylist(list):
    pass
a = Mylist()
print(type(a))
print(type(a) == list)
print(isinstance(a, list))