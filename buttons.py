from tkinter import * 

root = Tk()


def myCick(): 
    myLabel = Label(root, text="Clicked")
    
    myLabel.pack()
        
    
    

mybtn = Button(root, text="click me", padx=36, pady=36 , state="normal", command=myCick, fg="#a0aa0a", bg="#ffaaff")
mybtn.pack()

root.mainloop()