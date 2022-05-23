from tkinter import *

window = Tk()
window.title("grid test")

data = IntVar()
data.set(20)

h_label = Label(window, text="Height: ", font=("맑은고딕", 15), fg="#1f50b5")
h_entry = Entry(window, font=("맑은고딕", 15), width=10)

w_label = Label(window, text="Width: ", font=("맑은고딕", 15), fg="#1f50bb5")
w_entry = Entry(window, font=("맑은고딕", 15), width=10, bd=3, textvariable=data)

raw_image = PhotoImage(file="images/배경화면1.jpg")
image = Label(window, image=raw_image)

button1 = Button(window, text="Zoom In")
button2 = Button(window, text="Zoom Out")

h_label.grid(row=0, column=0, sticky=E)
w_label.grid(row=0, column=0, sticky=E)

h_entry.grid(row=0, column=0, ipadx=5, ipady=5)
w_entry.grid(row=0, column=0, ipadx=5, ipady=5)

image.grid(row=0, column=2, rowspan=2, columnspan=2, padx=10, pady=10)

button1.grid(row=2, column=2)
button2.grid(row=2, column=3)

window.mainloop()