import tkinter as tk
from random import randint

class MainWindow(tk.Tk):
    def __init__(self):
        super().__init__()

        self.hidden_num = randint(1, 101)
        self.guesses = 0

        self.geometry('300x300')
        self.valid = (self.register(self.validation), '%P')
        self.label = tk.Label(self, text='Введите число от 1 до 100:').pack()
        self.entry = tk.Entry(self, validate='key', validatecommand=self.valid)
        self.entry.pack()
        self.button1 = tk.Button(self, text='Продолжить', command=self.guess_check).pack()
        self.button2 = tk.Button(self, text='Заново', command=self.reset).pack()
        self.button3 = tk.Button(self, text='Показать количество попыток', command=self.show_guesses).pack()

        self.mainloop()

    def validation(self, new_value: str):
        if new_value.isnumeric():
            return int(new_value) in range(1, 101)
        else: return new_value == ''

    def reset(self):
        self.hidden_num = randint(1, 100)
        self.guesses = 0
        self.entry.delete(0, tk.END)

    def show_guesses(self):
        GuessesWindow(self.guesses)

    def guess_check(self):
        if self.entry.get() != '':
            self.guesses += 1
            CheckWindow(int(self.entry.get()), self.hidden_num, self.guesses)
            self.entry.delete(0, tk.END)

class GuessesWindow(tk.Toplevel):
    def __init__(self, guesses):
        super().__init__()

        self.label = tk.Label(self, text=f'Количество попыток - {guesses}').pack()

class CheckWindow(tk.Toplevel):
    def __init__(self, guess, right_num, guesses):
        super().__init__()

        self.guess = guess
        self.right_num = right_num
        self.guesses = guesses

        self.command = self.destroy

        if self.guess < self.right_num:
            self.text = f'Загаданное число больше {self.guess}'
            
        elif self.guess > self.right_num:
            self.text = f'Загаданное число меньше {self.guess}'
        else: 
            self.text = 'Это правильный ответ! Вы победили'
            self.command = exit

        self.label = tk.Label(self, text=self.text).pack()
        self.button = tk.Button(self, text='Продолжить', command=self.command).pack()


app = MainWindow()