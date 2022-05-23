from tkinter import *

window = Tk()

window.title("윈도우 창 연습")
window.geometry("400x400+100+0")    #너비 * 높이 + x좌표 + y좌표
window.resizable(True, False)       #창 크기 조절 방지(x축, y축)

label1 = Label(window, text="파이썬을")
label2 = Label(window, text="열심히", font=("함초롱바탕", 30), fg="#6799ff")
label3 = Label(window, text="공부 중입니다.", font=("맑은고딕", 15), bg="#ffd9ec", width=100, height=2, anchor=SE)

label1.pack()
label2.pack()
label3.pack()

window.mainloop()