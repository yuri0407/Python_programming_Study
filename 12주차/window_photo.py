from tkinter import *

window = Tk()

window.title("윈도우 창 연습")

photo = PhotoImage(file="images/배경화면1.jpg")
label1 = Label(window, image=photo)

photo2 = PhotoImage(file="images/배경화면2.jpg")
label2 = Label(window, image=photo2)

label1.pack(side=LEFT)
label2.pack()

window.mainloop()