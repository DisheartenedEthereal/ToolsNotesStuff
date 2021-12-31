from tkinter import *
from typing import Match
root = Tk()
root.title("very shitty calulator")
numbox = Entry(root,width=35,borderwidth=5)
numbox.grid(row=0,column=0,columnspan=3,pady=10,padx=10)
def button_click(number):
    #numbox.delete(0,END)
    curr = numbox.get()
    numbox.delete(0,END)
    numbox.insert(0,str(curr)+ str(number))
    return
def button_clear():
    numbox.delete(0,END)
def button_add():
    curr = numbox.get()
    global curr_g
    global math 
    math = "Addition"
    curr_g = int(curr)
    numbox.delete(0,END)
def button_equal():
    if math == "Addition":
        sec_curr = numbox.get()
        numbox.delete(0,END)
        numbox.insert(0, curr_g + int(sec_curr))
    elif math == "Division":
        sec_curr = numbox.get()
        numbox.delete(0,END)
        numbox.insert(0, curr_g / int(sec_curr))
    elif math == "Multiplication":
        sec_curr = numbox.get()
        numbox.delete(0,END)
        numbox.insert(0, curr_g * int(sec_curr))
    elif math == "Subtraction":
        sec_curr = numbox.get()
        numbox.delete(0,END)
        numbox.insert(0, curr_g - int(sec_curr))
    else:
        return
def button_divide():
    curr = numbox.get()
    global curr_g
    global math 
    math = "Division"
    curr_g = int(curr)
    numbox.delete(0,END)
    return
def button_subtract():
    curr = numbox.get()
    global curr_g
    global math 
    math = "Subtraction"
    curr_g = int(curr)
    numbox.delete(0,END)
    return

def button_multiply():
    curr = numbox.get()
    global curr_g
    global math 
    math = "Multiplication"
    curr_g = int(curr)
    numbox.delete(0,END)
    return
#button list
butt1 = Button(root,text="1",padx=40,pady=20,command=lambda: button_click(1))
butt2 = Button(root,text="2",padx=40,pady=20,command=lambda: button_click(2))
butt3 = Button(root,text="3",padx=40,pady=20,command=lambda: button_click(3))
butt4 = Button(root,text="4",padx=40,pady=20,command=lambda: button_click(4))
butt5 = Button(root,text="5",padx=40,pady=20,command=lambda: button_click(5))
butt6 = Button(root,text="6",padx=40,pady=20,command=lambda: button_click(6))
butt7 = Button(root,text="7",padx=40,pady=20,command=lambda: button_click(7))
butt8 = Button(root,text="8",padx=40,pady=20,command=lambda: button_click(8))
butt9 = Button(root,text="9",padx=40,pady=20,command=lambda: button_click(9))
butt0 = Button(root,text="0",padx=40,pady=20,command=lambda: button_click(0))

butt_add = Button(root,text="+",padx=39,pady=20,command=lambda: button_add())
butt_clear = Button(root,text="CLEAR",padx=79,pady=20,command=lambda: button_clear())
butt_equal = Button(root,text="=",padx=91,pady=20,command=lambda: button_equal())
butt_multiply = Button(root,text="*",padx=41,pady=20,command=lambda: button_multiply()).grid(row=6,column=0)
butt_subtract = Button(root,text="-",padx=40,pady=20,command=lambda: button_subtract()).grid(row=6,column=1)
butt_divide = Button(root,text="/",padx=40,pady=20,command=lambda: button_divide()).grid(row=6,column=2)
#buttons griding
butt1.grid(row=3,column=0)
butt2.grid(row=3,column=1)
butt3.grid(row=3,column=2)

butt4.grid(row=2,column=0)
butt5.grid(row=2,column=1)
butt6.grid(row=2,column=2)

butt7.grid(row=1,column=0)
butt8.grid(row=1,column=1)
butt9.grid(row=1,column=2)

butt0.grid(row=4,column=0)

butt_add.grid(row=5,column=0)
butt_clear.grid(row=4,column=1,columnspan=2)
butt_equal.grid(row=5,column=1,columnspan=2)
root.mainloop()