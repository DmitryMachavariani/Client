import tkinter
import package
from tkinter import messagebox

root = tkinter.Tk()
root.title("ЧАТ")
root.resizable(0, 0)

#Поля для аваторизации пользователя
label_username = tkinter.Label(root, text="Введите логин").grid(row=0, column=0)
username_auth = tkinter.Entry(root)
username_auth.grid(row=0, column=1)

label_password = tkinter.Label(root, text="Введите пароль").grid(row=1, column=0)
password_auth = tkinter.Entry(root)
password_auth.grid(row=1, column=1)

button_auth = tkinter.Button(root, text="Войти")
button_auth.grid(row=1, column=2)
button_auth.bind("<Button-1>", lambda event: messagebox.askquestion("Сообщение", package.buildpackage("login", [username_auth.get(), password_auth.get()])))

root.mainloop()
