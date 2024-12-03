import json
import requests
from tkinter import *
from tkinter import messagebox

root = Tk()
root.geometry("500x400")
root.title("Git request")


def request():
    url = f"https://api.github.com/repos/{for_username.get()}/{for_repository_name.get()}"
    user_data = requests.get(url).json()

    task = {"company": user_data.get("owner").get("company"),
            "created_at": user_data.get("created_at"),
            "email": user_data.get("email"),
            "id": user_data.get("id"),
            "name": user_data.get("owner").get("name"),
            "url": user_data.get("owner").get("url")}

    with open("result.txt", "w") as result:
        json.dump(task, result)

    messagebox.showinfo("Успешно", "Результат запроса находится в файле - result.txt")


text_username = Label(root, text="Введите автора репозитория:    ", width=24)
text_username.grid(column=0, row=0)

for_username = Entry(root, width=16)
for_username.grid(column=1, row=0)

text_repository_name = Label(root, text="Введите название репозитория:", width=24)
text_repository_name.grid(column=0, row=1)

for_repository_name = Entry(root, width=16)
for_repository_name.grid(column=1, row=1)

button = Button(root, text="Выполнить запрос", command=request, width=24)
button.grid(column=0, row=2)

root.mainloop()
