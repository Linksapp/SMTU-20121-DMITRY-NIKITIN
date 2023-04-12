class Box:
    def add(self):
        raise NotImplementedError('Метод add не переопределен')
    def empty(self):
        raise NotImplementedError('Метод empty не переопределен')
    def count(self):
        raise NotImplementedError('Метод count не переопределен')

class Item:
    def __init__(self, value):
        self.name = self
        self.value = value

class ListBox(Box):
    def __init__(self, elements_amount):
        self.elements = [Item(x) for x in range(elements_amount)]
        # print(self.elements)
    def add(self, element):
        try: self.elements.extend(element)
        except: self.elements.append(element)
    def empty(self):
        a = self.elements
        self.elements = []
        return a
    def count(self):
        return len(self.elements)

class DictBox(Box):
    def __init__(self, elements_amount):
        self.source = [Item(x) for x in range(elements_amount)]
        self.elements = {f'{elem}':elem for elem in self.source}
    def add(self, elements):
        try: 
            for elem in elements:
                self.elements[f'{elem}'] = elem
        except: self.elements[f'{elements}'] = elements
    def empty(self):
        a = self.elements
        self.elements = {}
        return list(a.values())
    def count(self):
        return len(self.elements)

def repack_boxes(*args):
    elements = []
    for box in args:
        elements.extend(box.empty())
    int_amount = int(len(elements) / len(args))
    for box in args:
        box.add(elements[:int_amount])
        elements = elements[int_amount:]
    for box in args:
        if elements == []:
            break
        box.add(elements.pop())
        

repack_boxes(ListBox(20), ListBox(9), DictBox(6))