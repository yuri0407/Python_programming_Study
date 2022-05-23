from tkinter import *

window = Tk()

Label(window, text="박스 #1", bg="red", fg="white").place(x=0, y=0)
Label(window, text="박스 #2", bg="greed", fg="white").place(x=20, y=20)
Label(window, text="박스 #3", bg="blue", fg="white").place(x=40, y=40)

window.mainloop()