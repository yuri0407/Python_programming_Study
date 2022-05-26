from tkinter import *

def show():
    print("아이디 : %s \n비밀번호 : %s" % (e1.get(), e2.get()))
    e1.insert(END, 3.5)

window = Tk()
window.title("로그인")
window.geometry("300x150")

Label(window, text="아이디").place(x=20, y=20)
Label(window, text="비밀번호").place(x=20, y=50)

e1 = Entry(window)
e2 = Entry(window, show="*")

e1.place(x=80, y=20)
e2.place(x=80, y=50)

Button(window, text="로그인", command=show).place(x=70, y=80)
Button(window, text="종료", command=quit).place(x=170, y=80)
window.mainloop()