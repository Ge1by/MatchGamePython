from tkinter import *
import random
from tkinter import messagebox

root = Tk()
root.title("Match Game")
root.geometry("500x500")

global winner, matches
# Счетчик побед
winner = 0

# Создаем пары
matches = [1, 1, 2, 2, 3, 3, 4, 4, 5, 5, 6, 6]
# Перемешиваем созданые пары
random.shuffle(matches)

# Создаем окно кнопки
my_frame = Frame(root)
my_frame.pack(pady=10)

# Инициализация некоторых переменных
count = 0
answer_list = []
answer_dict = {}


# Перезапуск игры
def reset():
    global matches, winner
    winner = 0
    # Создаем пары
    matches = [1, 1, 2, 2, 3, 3, 4, 4, 5, 5, 6, 6]
    # Перемешиваем созданые пары
    random.shuffle(matches)

    # Сброс my_label
    my_label.config(text="")

    # Сброс клеток
    button_list = [b0, b1, b2, b3, b4, b5, b6, b7, b8, b9, b10, b11]
    # Меняем цвет всем кнопкам
    for button in button_list:
        button.config(text=" ", bg="SystemButtonFace", state="normal")


# Функция победы в игре
def win():
    my_label.config(text="Поздравляем, вы победили!")
    button_list = [b0, b1, b2, b3, b4, b5, b6, b7, b8, b9, b10, b11]
    # Меняем цвет всем кнопкам на золотой
    for button in button_list:
        button.config(bg="#FFD700")


# Функция для нажатия кнопок
def button_click(b, number):
    global count, answer_list, answer_dict, winner

    if b["text"] == " " and count < 2:
        b["text"] = matches[number]
        # Добавление номера в answer_list
        answer_list.append(number)
        # Добавление кнопки и номера в answer_dict
        answer_dict[b] = matches[number]
        # увеличение счетчика
        count += 1

    # Начинаем определять правильно или нет
    if len(answer_list) == 2:
        if matches[answer_list[0]] == matches[answer_list[1]]:
            my_label.config(text="Совпало!")
            for key in answer_dict:
                key["state"] = "disabled"
            count = 0
            answer_list = []
            answer_dict = {}
            # Увеличиваем счетчик победителя
            winner += 1
            if winner == 6:
                win()
        else:
            my_label.config(text=" ")
            count = 0
            answer_list = []
            # всплывающее окно
            messagebox.showinfo("Неправильно!", "Неправильно")

            # сброс кнопок
            for key in answer_dict:
                key["text"] = " "

            answer_dict = {}


# Инициализация кнопок
b0 = Button(my_frame, text=" ", font=("Helvetica", 20), height=3, width=6, command=lambda: button_click(b0, 0),
            relief="ridge")
b1 = Button(my_frame, text=" ", font=("Helvetica", 20), height=3, width=6, command=lambda: button_click(b1, 1),
            relief="ridge")
b2 = Button(my_frame, text=" ", font=("Helvetica", 20), height=3, width=6, command=lambda: button_click(b2, 2),
            relief="ridge")
b3 = Button(my_frame, text=" ", font=("Helvetica", 20), height=3, width=6, command=lambda: button_click(b3, 3),
            relief="ridge")
b4 = Button(my_frame, text=" ", font=("Helvetica", 20), height=3, width=6, command=lambda: button_click(b4, 4),
            relief="ridge")
b5 = Button(my_frame, text=" ", font=("Helvetica", 20), height=3, width=6, command=lambda: button_click(b5, 5),
            relief="ridge")
b6 = Button(my_frame, text=" ", font=("Helvetica", 20), height=3, width=6, command=lambda: button_click(b6, 6),
            relief="ridge")
b7 = Button(my_frame, text=" ", font=("Helvetica", 20), height=3, width=6, command=lambda: button_click(b7, 7),
            relief="ridge")
b8 = Button(my_frame, text=" ", font=("Helvetica", 20), height=3, width=6, command=lambda: button_click(b8, 8),
            relief="ridge")
b9 = Button(my_frame, text=" ", font=("Helvetica", 20), height=3, width=6, command=lambda: button_click(b9, 9),
            relief="ridge")
b10 = Button(my_frame, text=" ", font=("Helvetica", 20), height=3, width=6, command=lambda: button_click(b10, 10),
             relief="ridge")
b11 = Button(my_frame, text=" ", font=("Helvetica", 20), height=3, width=6, command=lambda: button_click(b11, 11),
             relief="ridge")

# Делаем сетку из кнопок
b0.grid(row=0, column=0)
b1.grid(row=0, column=1)
b2.grid(row=0, column=2)
b3.grid(row=0, column=3)

b4.grid(row=1, column=0)
b5.grid(row=1, column=1)
b6.grid(row=1, column=2)
b7.grid(row=1, column=3)

b8.grid(row=2, column=0)
b9.grid(row=2, column=1)
b10.grid(row=2, column=2)
b11.grid(row=2, column=3)

my_label = Label(root, text="")
my_label.pack(pady=20)

# Создаем меню
my_menu = Menu(root)
root.config(menu=my_menu)

# Создаем выпадающее меню настроек
options_menu = Menu(my_menu, tearoff=False)
my_menu.add_cascade(label="Настройки", menu=options_menu)
options_menu.add_command(label="Перезапустить игру", command=reset)
options_menu.add_separator()
options_menu.add_command(label="Выйти из игры", command=root.quit)

root.mainloop()