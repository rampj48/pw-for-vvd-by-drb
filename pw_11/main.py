from tkinter import *
from tkinter import ttk
from tkinter.ttk import Combobox
from tkinter import filedialog

root = Tk()
root.title("Богданов Д.Р.")
root.geometry("400x300")

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
def clicked():
    res = []
    count = 0
    if status1.get() == 1:
        count += 1
        res.append("Первый")
    if status2.get() == 1:
        count += 1
        res.append("Второй")
    if status3.get() == 1:
        count += 1
        res.append("Третий")

    str_res = ""
    for word in res:
        if len(res) > 1:
            str_res += word + ", "
        else:
            str_res += word + "  "

    choose.set(f"Вы выбрали: {str_res[:-2]}")


label_checkbox = Label(tab_checkbox, text="Чекбоксы")
label_checkbox.grid(column=0, row=0)

choose = StringVar()
label_choose = Label(textvariable=choose)
label_choose.pack()

status1 = BooleanVar()
check1 = Checkbutton(tab_checkbox, text="Первый", variable=status1, command=clicked)
check1.grid(column=0, row=1)

status2 = BooleanVar()
check2 = Checkbutton(tab_checkbox, text="Второй", variable=status2, command=clicked)
check2.grid(column=0, row=2)

status3 = BooleanVar()
check3 = Checkbutton(tab_checkbox, text="Третий", variable=status3, command=clicked)
check3.grid(column=0, row=3)

# Текстовый редактор
label_text = Label(tab_text, text="Текстовый редактор")
label_text.grid(column=0, row=0)
text_editor = Text()
text_editor.pack(fill=BOTH, expand=True)


def upload_file():
    file_path = filedialog.askopenfilename()
    if file_path != "":
        with open(file_path, "r") as file:
            text = file.read()
            text_editor.delete("1.0", END)
            text_editor.insert("1.0", text)


def save_file():
    file_path = filedialog.asksaveasfilename()
    if file_path != "":
        text = text_editor.get("1.0", END)
        with open(file_path, "w") as file:
            file.write(text)


open_button = Button(tab_text, text="Открыть файл", command=upload_file)
open_button.grid(column=0, row=1)
save_button = Button(tab_text, text="Сохранить файл", command=save_file)
save_button.grid(column=1, row=1)

root.mainloop()
