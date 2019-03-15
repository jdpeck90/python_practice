from tkinter import *

window = Tk()


def km_to_miles():
    miles = float(el_value.get())*1.6
    tl.insert(END, miles)


b1 = Button(window, text="Execute", command=km_to_miles)
b1.grid(row=0, column=0)


el_value = StringVar()
el = Entry(window, textvariable=el_value)
el.grid(row=0, column=1)


tl = Text(window, height=1, width=20)
tl.grid(row=0, column=2)
window.mainloop()
