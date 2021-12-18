from tkinter import *
from random import randint

isBlocked = False
money = 0
def clicked():
    global isBlocked
    global money
    if isBlocked == False:
        sum = int(txt.get())
        if sum > 0:
            isBlocked = True
            res = "Ваш баланс: {}".format(sum)
            lbl.configure(text=res)
            btn.configure(text = 'Преумножить')
            txt.delete(0, 'end')
            money = sum
    else:
        if money > 0:
            sum = money
            val1 = randint(0, 9)
            val2 = randint(0, 9)
            val3 = randint(0, 9)

            texttoprint = 'Вы проиграли 100'
            if val1 == val2 == val3:
                sum = sum * 1000
                texttoprint = 'Вы выйграли миллион!'
            elif val1 == val2:
                sum += 3
                texttoprint = 'Вы выйграли 3!'
            elif val1 == val3:
                sum += 3
                texttoprint = 'Вы выйграли 3!'
            elif val2 == val3:
                sum += 3
                texttoprint = 'Вы выйграли 3!'
            else:
                sum -= 100

            money = max(sum, 0)
            res = "Ваш баланс: {}".format(money)
            lbl.configure(text=res)
            lbl1.configure(text=texttoprint)
            res1 = 'Вам выпало: {}, {}, {}'.format(val1, val2, val3)
            lbl2.configure(text = res1)

            if money == 0:
                btn.grid_remove()

                text = Label(window, text='Вы въебали все деньги')
                text.grid(column=2, row=0)



window = Tk()
window.title("Добро пожаловать в безпройгрышное казино от Карена")
window.geometry('600x400')

lbl = Label(window, text="Введите сумму, которую хотите преумножить: ")
lbl.grid(column=0, row=0)
txt = Entry(window, width=10)
txt.grid(column=1, row=0)
btn = Button(window, text="Сделать ставку", command=clicked)
btn.grid(column=2, row=0)
lbl1 = Label(window, text='')
lbl1.grid(column=0, row=1, padx=10, pady=10)
lbl2 = Label(window, text='')
lbl2.grid(column=1, row=1, padx=50, pady=10)

window.mainloop()