from tkinter import *

window = Tk()

b1 = Button(window, text="Execute")
b1.grid(row=0, column=0)


el = Entry(window)
el.grid(row=0, column=1)


tl = Text(window, height=20)
tl.grid(row=0, column=2)
window.mainloop()
