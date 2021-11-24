from tkinter import *


def buy():
    select = list(shop.curselection())
    select.reverse()
    for i in select:
       order.insert(0, shop.get(i))
    for i in select:
        shop.delete(i)

def Return():
    select = list(order.curselection())
    select.reverse()
    for i in select:
        shop.insert(0, order.get(i))
    for i in select:
        order.delete(i)

root = Tk()

food = ['apple', 'bananas', 'tomato', 'potato', 'carrot', 'pineapple', 'bread', 'butter', 'milk', 'meat']

shop = Listbox(selectmode=EXTENDED)
for i in food:
    shop.insert(0, i)
shop.pack(side=LEFT)


f = Frame()
f.pack(side=LEFT)

b1 = Button(f, text = '>>>', command = buy).pack()
b2 = Button(f, text = '<<<', command = Return).pack()

order = Listbox(selectmode = EXTENDED)
order.pack(side=LEFT)

root.mainloop()
