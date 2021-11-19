from tkinter import *


def phone_number():
    v = var.get()
    if v == 0:
        label['text'] = '+9 2124567892'
    elif v == 1:
        label['text'] = '+4 9087654321'
    elif v == 2:
        label['text'] = '+8 2123120321'


root = Tk()

f = Frame()
f.pack(side=LEFT)

var = IntVar()
var.set(-1)
Radiobutton(f, text="Вася", width=10, height=3,
            indicatoron=0, variable=var,
            value=0, command=phone_number).pack()
Radiobutton(f, text="Петя", width=10, height=3,
            indicatoron=0, variable=var,
            value=1, command=phone_number).pack()
Radiobutton(f, text="Маша", width=10, height=3,
            indicatoron=0, variable=var,
            value=2, command=phone_number).pack()

label = Label (width=20)
label.pack(side=LEFT, fill=Y)

root.mainloop()
