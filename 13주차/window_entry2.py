from tkinter import *

def show():
    print("이름 : %s \n나이 : %s" % (e1.get(), e2.get()))
    e1.insert(END, 3.5)

window = Tk()
window.geometry("300x150")

Label(window, text="이름").place(x=20, y=20)
Label(window, text="나이").place(x=20, y=50)

e1 = Entry(window)
e2 = Entry(window, show="*")

e1.place(x=60, y=20)
e2.place(x=60, y=50)

Button(window, text="보이기", command=show).place(x=70, y=80)
Button(window, text="종료", command=quit).place(x=170, y=80)
window.mainloop()