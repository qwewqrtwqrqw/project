from tkinter import *
from tkinter import messagebox


def function():
    currency_rate = 72.2853 # Курс высчитан из ТЗ, 5000 RUB / 69.1703 USD
    money = float(input_field.get(1.0,END))
    output = ''
    
    second_currency = ''
    if var.get() == 0:
        currency = 'RUB'
        second_currency = 'USD'
        output = str(money)+' '+currency+' = '+str(round(money/currency_rate,4))+' '+second_currency
        
    elif var.get() == 1:
        currency = 'USD'
        second_currency = 'RUB'
        output = str(money)+' '+currency+' = '+str(round(money*currency_rate,4))+' '+second_currency
        
    else:
        messagebox.showerror('Ошибка', 'Ошибка!')
    output_field.delete(1.0, END)
    output_field.insert(1.0, output)
    
    with open('Changelog.txt', 'a') as file:
        file.write(output+'\n')

# Элементы интерфейса, отвечающие за основное окно
main_win = Tk()
main_win.title("Рассчёт по курсу доллара")
main_win.configure(background = 'light gray')
main_win.geometry("384x208")
main_win.resizable(height = 0, width = 0)


# Элементы интерфейса, отвечающие за ввод переменной money
label2 = Label(main_win,text = 'Введите нужную сумму: ',bg = "white")
label2.grid(row = 0, column = 0, padx = 15, pady = 15, sticky = W)

input_field = Text(main_win, height = 2, width = 20, font = "lucida 10",)
input_field.grid(row = 1, column = 0, padx = 15, sticky = W)


# Элементы интерфейса, отвечающие за выбор валюты
label = Label(main_win, text = 'Выберите валюту:',bg = "white")
label.grid(row = 2, column = 0, padx = 15, pady = 15, sticky = W)

var=IntVar()
var.set(0)
rad0 = Radiobutton(main_win, text="RUB", variable=var, value=0,bg = "white")
rad0.grid(row = 3, column = 0, padx = 15, sticky = W)

rad1 = Radiobutton(main_win, text="USD", variable=var, value=1,bg = "white")
rad1.grid(row = 4, column = 0, padx = 15, sticky = W)


# Элементы интерфейса, отвечающие за вывод итоговой величины 
label4 = Label(main_win, text = '   Поле для вывода:   ',bg = "white")
label4.grid(row = 0, column = 2, pady = 15)

output_field = Text(main_win, height = 2, width = 25, font = "lucida 10",)
output_field.grid(row = 1, column = 2, padx = 15, sticky = E)

button = Button(main_win,text = "Ввод",bg = "white",command = function)
button.grid(row = 2, column = 2, pady = 15)

main_win.mainloop()