from ast import Lambda
from tkinter import * 


root = Tk()

root.title("Caclulator")
e = Entry(root, width=35, borderwidth=5)
e.grid(row=0, column=0, columnspan=3)

def button_click(number):
    
    current = e.get()

    e.delete(0, END)
    e.insert(0,str(current)+ str(number))
    return

def button_clear():
    e.delete(0,END)
    
    return

def button_add():
    first_number = e.get()
    global f_num 
    global math
    math = "addition"
    f_num = int(first_number)
    e.delete(0,END)
    return 

def button_equal():
    second_number = e.get()
    e.delete(0,END)

    if math == "addition":
        e.insert(0,f_num + int(second_number))
    if math == "multiplication":
        e.insert(0,f_num * int(second_number))
    if math == "substraction":
        e.insert(0,f_num - int(second_number))
    if math == "division":
        e.insert(0,f_num / int(second_number))    
 

def button_mul():
    first_number = e.get()
    global f_num 
    global math
    math = "multiplication"
    f_num = int(first_number)
    e.delete(0,END)
    return 

def button_sub():
    first_number = e.get()
    global f_num 
    global math
    math = "substraction"
    f_num = int(first_number)
    e.delete(0,END)
    return 

def button_div():
    first_number = e.get()
    global f_num 
    global math
    math = "division"
    f_num = int(first_number)
    e.delete(0,END)
    return 


button_1 = Button(root, text="1", padx="40", pady="20", command=lambda: button_click(1))
button_2 = Button(root, text="2", padx="40", pady="20", command=lambda: button_click(2))
button_3 = Button(root, text="3", padx="40", pady="20", command=lambda: button_click(3))
button_4 = Button(root, text="4", padx="40", pady="20", command=lambda: button_click(4))
button_5 = Button(root, text="5", padx="40", pady="20", command=lambda: button_click(5))
button_6 = Button(root, text="6", padx="40", pady="20", command=lambda: button_click(6))
button_7 = Button(root, text="7", padx="40", pady="20", command=lambda: button_click(7))
button_8 = Button(root, text="8", padx="40", pady="20", command=lambda: button_click(8))
button_9 = Button(root, text="9", padx="40", pady="20", command=lambda: button_click(9))
button_0 = Button(root, text="0", padx="40", pady="20", command=lambda: button_click(0))

btn_add = Button(root, text="+", padx="39", pady="20", command=button_add)
btn_equal = Button(root, text="=", padx="91", pady="20", command=button_equal)
btn_clear = Button(root, text="Clear", padx="79", pady="20", command=button_clear)

btn_substract = Button(root, text="-", padx="40", pady="20", command=button_sub)
btn_multiply = Button(root, text="*", padx="40", pady="20", command=button_mul)
btn_divide = Button(root, text="/", padx="40", pady="20", command=button_div)

btn_substract.grid(row=6, column=0)
btn_multiply.grid(row=6, column=1)
btn_divide.grid(row=6, column=2)

button_1.grid(row=3 , column =0)
button_2.grid(row=3 , column =1)
button_3.grid(row=3 , column =2)

button_4.grid(row=2 , column =0)
button_5.grid(row=2 , column =1)
button_6.grid(row=2 , column =2)

button_7.grid(row=1 , column =0)
button_8.grid(row= 1, column =1)
button_9.grid(row= 1, column =2)

button_0.grid(row=4 , column =0)

btn_add.grid(row= 5 , column=0)
btn_clear.grid(row=5, column=1, columnspan=2)
btn_equal.grid(row=4, column=1, columnspan=2)

root.mainloop()
