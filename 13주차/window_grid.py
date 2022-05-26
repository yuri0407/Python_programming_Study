from tkinter import *

window = Tk()
window.geometry("200x200")

b1 = Button(window, text="one")
b2 = Button(window, text="two")
b3 = Button(window, text="three")

b1.grid(row=0, column=0, rowspan=2)
b2.grid(row=1, column=1)
b3.grid(row=0, column=2)

window.mainloop()