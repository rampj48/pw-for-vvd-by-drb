from tkinter import *
from tkinter import ttk
from tkinter.ttk import Combobox

root = Tk()
root.title("Богданов Д.Р.")
root.geometry("400x250")

tab_control = ttk.Notebook(root)
tab_calculator = ttk.Frame(tab_control)
tab_checkbox = ttk.Frame(tab_control)
tab_text = ttk.Frame(tab_control)

tab_control.add(tab_calculator, text="Первая вкладка")
tab_control.add(tab_checkbox, text="Вторая вкладка")
tab_control.add(tab_text, text="Третья вкладка")
tab_control.pack(expand=1, fill="both")


# Калькулятор
def calculate():
    number1 = int(first_number.get())
    sing = operation_sign.get()
    number2 = int(second_number.get())
    res = 0

    if sing == "+":
        res = number1 + number2
    elif sing == "-":
        res = number1 - number2
    elif sing == "*":
        res = number1 * number2
    elif sing == "/":
        if number2 == 0:
            res = "На ноль делить нельзя!"
        else:
            res = number1 // number2

    result.config(text=str(res))


label_calculator = Label(tab_calculator, text="Калькулятор")
label_calculator.grid(column=0, row=0)

first_number = Entry(tab_calculator, width=12)
first_number.grid(column=0, row=1)

sings = ["+", "-", "*", "/"]
operation_sign = Combobox(tab_calculator, values=sings, width=1)
operation_sign.grid(column=1, row=1)

second_number = Entry(tab_calculator, width=12)
second_number.grid(column=2, row=1)

equals = Button(tab_calculator, text=" = ", command=calculate)
equals.grid(column=3, row=1)

result = Label(tab_calculator)
result.grid(column=4, row=1)

# Чекбоксы
label_checkbox = Label(tab_checkbox, text="Чекбоксы")
label_checkbox.grid(column=0, row=0)

root.mainloop()
