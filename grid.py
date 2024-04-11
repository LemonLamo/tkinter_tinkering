from tkinter import * 

root = Tk()
# create a label with text 
myLabel = Label(root, text="Hello World")
myLabel2 = Label(root, text="Hello World 2")
#packing : shoving shit on the scrreeen 

myLabel.grid(row=0, column=0, rowspan=3, ipady=100 , ipadx=100)

myLabel2.grid(row=3 , column=1)
# create an event loop 

root.mainloop()