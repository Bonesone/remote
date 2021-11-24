from tkinter import *

def replace(event):
    select = list(e1.get())
    select.reverse()
    for i in select:
        b.insert(0, i)
        e1.delete(0, END)
    
def copy(event):
    select = list(b.curselection())
    select.reverse()
    for i in select:
        e1.delete(0, END)
        e1.insert(0, b.get(i))
    

root = Tk()

e1 = Entry()
e1.bind('<Return>', replace)
e1.pack(pady = 5, padx = 5)

b = Listbox()
b.bind('<Double-Button-1>', copy)
b.pack()
 
root.mainloop()