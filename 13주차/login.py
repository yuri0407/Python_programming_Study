from tkinter import *

def show():
    print("아이디 : %s \n비밀번호 : %s" % (e1.get(), e2.get()))

window = Tk()
window.title("로그인")
window.geometry("400x200")

frame1 = Frame(window, height=55)
frame1.grid(row=0)

frame2 = Frame(window, height=40)
frame2.grid(row=1)

frame3 = Frame(window, width=60)
frame3.grid(column=0, row=0)

frame4 = Frame(window, width=10)
frame4.grid(column=3, row=1, rowspan=2)

label1 = Label(window, text="ID")
label2 = Label(window, text="PASSWORD")

label1.grid(row=1, column=1)
label2.grid(row=2, column=1)

e1 = Entry(window)
e2 = Entry(window, show="*")

e1.grid(row=1, column=2, ipady=2)
e2.grid(row=2, column=2, ipady=2)

btn = Button(window, text="login", command=show, height=2)
btn.grid(row=1, column=4, rowspan=2)

window.mainloop()