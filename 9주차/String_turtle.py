import tkinter
import turtle as t

swidth, sheight = 300, 300
txtSize = 30
t.shape("turtle")
t.setup(width = swidth+50, height = sheight+50)
t.screensize(swidth, sheight)

retStr = tkinter.simpledialog.askstring("Input char", "Input for turtle")
t.write(retStr, font=("맑은 고딕", txtSize, "bold"))

t.done() 