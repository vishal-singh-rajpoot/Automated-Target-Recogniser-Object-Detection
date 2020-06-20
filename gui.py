from tkinter import *
import os
def click():
    os.system("realtime.py")
def click1():
    os.system("img.py")
window=Tk()
window.title("OBJDECT")
window.configure(background='grey')
window.geometry("425x600")
Label(window,text="Please Select one button").place(x=10,y=500)
Button(window,text="Real Time",width=8,command=click).place(x=300,y=525)
Button(window,text="picture",width=8,command=click1).place(x=200,y=525)

window.mainloop()
