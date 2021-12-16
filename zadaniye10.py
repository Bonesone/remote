from tkinter import *
 
def motion():
  x = can.coords(ball)[2]
  y = can.coords(ball)[3]
  if can.x == x and can.y == y:
    return
  if can.x < x:
    can.move(ball,-1, 0)
  if can.x > x:
    can.move(ball, 1, 0)
  if can.y < y:
    can.move(ball, 0,-1)
  if can.y > y:
    can.move(ball, 0, 1)
  root.after(10, motion)
 
def click(event):
  can.x = event.x + 20
  can.y = event.y + 20
  motion()

root = Tk()
can = Canvas(root, width=300, height=200, bg="white")
can.pack()

ball = can.create_oval(0, 100, 40, 140, fill='green')

can.bind("<Button-1>", click)

root.mainloop()