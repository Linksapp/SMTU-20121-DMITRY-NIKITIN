import tkinter as tk


class MainWindow(tk.Tk):
    def __init__(self):
        super().__init__()
        self.dyn_list = []

        self.button1 = tk.Button(self, text='Создание списка', command=self.create_list).grid(row=0, sticky='WE')
        self.button2 = tk.Button(self, text='Вывод списка в консоль', command=self.consol_print).grid(row=1, sticky='WE')
        self.button3 = tk.Button(self, text='Запись списка в файл', command=self.write_to_file).grid(row=2, sticky='WE')
        self.button4 = tk.Button(self, text='Количество элементов в списке', command=self.list_len).grid(row=3, sticky='WE')
        self.button5 = tk.Button(self, text='Добавление элемента в список', command=self.extend_list).grid(row=4, sticky='WE')
        self.button6 = tk.Button(self, text='Поиск элемента в списке', command=self.find_item).grid(row=5, sticky='WE')
        self.button7 = tk.Button(self, text='Удаление элемента из списка', command=self.del_item).grid(row=6, sticky='WE')
        self.button8 = tk.Button(self, text='Выход', command=self.destroy).grid(row=7)

        self.mainloop()
    
    def create_list(self):
        self.window = CreateWindow()
        self.dyn_list = self.window.out_list
    
    def consol_print(self):
        print(self.dyn_list)

    def write_to_file(self):
        with open('semester 2/pr2/file.txt', 'w') as f:
            f.write(str(self.dyn_list))
    
    def list_len(self):
        self.window = LenWindow(len(self.dyn_list))

    def extend_list(self):
        self.window = ExtendWindow(self.dyn_list)
        self.dyn_list = self.window.out_list

    def find_item(self):
        self.window = FindWindow(self.dyn_list)

    def del_item(self):
        self.window = DelWindow(self.dyn_list)
        self.dyn_list = self.window.del_list

class CreateWindow(tk.Toplevel):
    def __init__(self):
        super().__init__()

        self.out_list = []

        self.text = tk.Label(self, text='Введите элементы списка (через пробел):').grid(row=0)
        self.entry = tk.Entry(self)
    
        self.button = tk.Button(self, text='Продолжить', command=self.make_list).grid(row=2)
        self.entry.grid(row=1, sticky='WE')
        self.out_list = self.entry.get().split()

    def make_list(self):
        self.out_list.extend(self.entry.get().split())
        self.destroy()
    

class LenWindow(tk.Toplevel):
    def __init__(self, len):
        super().__init__()
        self.text = tk.Label(self, text=f'Количество элементов в списке: {len}').grid(row=0)
        self.button = tk.Button(self, text='Продолжить', command=self.destroy).grid(row=1)

class ExtendWindow(tk.Toplevel):
    def __init__(self, dyn_list):
        super().__init__()

        self.out_list = dyn_list

        self.text = tk.Label(self, text='Введите элементы, которые хотите добавить (через пробел):').grid(row=0)
        self.entry = tk.Entry(self)
    
        self.button = tk.Button(self, text='Продолжить', command=self.extend_list).grid(row=2)
        self.entry.grid(row=1, sticky='WE')
    
    def extend_list(self):
        self.out_list.extend(self.entry.get().split())
        # print(self.out_list)
        self.destroy()

class FindWindow(tk.Toplevel):
    def __init__(self, dyn_list):
        super().__init__()

        self.find_list = dyn_list

        self.text = tk.Label(self, text='Введите искомый элемент:').grid(row=0)
        self.entry = tk.Entry(self)
    
        self.button = tk.Button(self, text='Продолжить', command=self.find_item).grid(row=2)
        self.entry.grid(row=1, sticky='WE')

    def find_item(self):
        self.search = self.entry.get()

        if self.search in self.find_list:
            print(f'Первое вхождение элемента находится по индексу - {self.find_list.index(self.search)}')
        else:
            print('Искомый элемент в списке не найден')
        

class DelWindow(tk.Toplevel):
    def __init__(self, dyn_list):
        super().__init__()

        self.del_list = dyn_list
        self.text = tk.Label(self, text='Выберете элемент, который надо удалить:').grid(row=0, columnspan=3)
        self.column = 0
        self.row = 1
        for i in range(len(self.del_list)):
            if self.column > 2:
                self.column = 0
                self.row += 1

            self.button = tk.Button(self, text=f'{self.del_list[i]}', command=lambda x = i: self.delete_item(x))
            self.button.grid(row=self.row, column=self.column, sticky='WE')
            self.column += 1

    def delete_item(self, indx):
        self.del_list.pop(indx)
        self.destroy()


app = MainWindow()