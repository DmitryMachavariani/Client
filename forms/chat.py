import tkinter
import package
import tempfile
import os


root = tkinter.Tk()
root.title("ЧАТ")
root.resizable(0, 0)

messagebox = tkinter.Text()
messagebox.grid(row=1, column=0)

input = tkinter.Entry(width=70)
input.grid(row=2, column=0)

btn = tkinter.Button(width=20, text="Отправить сообщение")
btn.grid(row=2, column=1)

lbl = tkinter.Label(text="Ваши друзья")
lbl.grid(row=0, column=1)

listbox = tkinter.Listbox(height=22)
listbox.grid(row=1, column=1)

path = os.path.join(tempfile.gettempdir(), "rieugbreifnre")
if(os.path.exists(path)):
    file = open(path, "rb")
    username = file.read().decode('UTF-8')

res = package.buildpackage("getfriend", [username])
print(res)
for i in res:
    listbox.insert(0, i)

root.mainloop()
