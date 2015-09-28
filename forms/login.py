import tkinter
import package
import tempfile
import os
from tkinter import messagebox


def login(event):
    username = username_auth.get()
    password = password_auth.get()

    res = package.buildpackage("login", [username, password])

    if res[0] == "login":
        if res[1] == "success":
            messagebox.showinfo("Сообщение", "Успешно вошли")
            tmp = os.path.join(tempfile.gettempdir(), "rieugbreifnre")
            file = open(tmp, "wb")
            file.write(username.encode('UTF-8'))
            file.close()

            root.destroy()
            import forms.chat
        else:
            messagebox.askquestion("Сообщение", "Неправильно ввели данные")


root = tkinter.Tk()
root.title("ЧАТ")
root.resizable(0, 0)

# Поля для аваторизации пользователя
label_username = tkinter.Label(root, text="Введите логин").grid(row=0, column=0)
username_auth = tkinter.Entry(root)
username_auth.grid(row=0, column=1)
username_auth.insert(0, "angus123")

label_password = tkinter.Label(root, text="Введите пароль").grid(row=1, column=0)
password_auth = tkinter.Entry(root)
password_auth.grid(row=1, column=1)
password_auth.insert(0, "159357")

button_auth = tkinter.Button(root, text="Войти")
button_auth.grid(row=1, column=2)
button_auth.bind("<Button-1>", login)

root.mainloop()
