from tkinter import * 

root = Tk()

e = Entry(root, width=50, bg="#c1a2e4", borderwidth=2,state="readonly")
e.pack()

e2 = e = Entry(root, width=50, bg="#c1a2e4", borderwidth=2,state='normal')
e2.pack()
e2.insert(0,"Enter yoru name")
def myCick(): 
    myLabel = Label(root, text=e2.get())
    
    myLabel.pack()
    
mybtn = Button(root, text="click me", padx=36, pady=36 , state="normal", command=myCick, fg="#a0aa0a", bg="#ffaaff")
mybtn.pack()

root.mainloop()