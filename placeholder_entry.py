import tkinter as tk

class PlaceholderEntry(tk.Entry):
    def __init__(self, master=None, placeholder='', cnf={}, fg='black',
                 fg_placeholder='grey50', *args, **kw):
        super().__init__(master=None, cnf={}, bg='white', *args, **kw)
        self.fg = fg
        self.fg_placeholder = fg_placeholder
        self.placeholder = placeholder
        self.bind('<FocusOut>', lambda event: self.fill_placeholder())
        self.bind('<FocusIn>', lambda event: self.clear_box())
        self.fill_placeholder()

    def clear_box(self):
        if not self.get() and super().get():
            self.config(fg=self.fg)
            self.delete(0, tk.END)

    def fill_placeholder(self):
        if not super().get():
            self.config(fg=self.fg_placeholder)
            self.insert(0, self.placeholder)
    
    def get(self):
        content = super().get()
        if content == self.placeholder:
            return ''
        return content

class App(tk.Frame):
    def __init__(self, master=None):
        self.root = master
        super().__init__(master, borderwidth=0, relief=tk.RAISED)
        
        self.root.title('Placeholder example')
        self.pack_propagate(False)
        self.pack()
        
        self.entry = PlaceholderEntry(self.root, placeholder='This text is a placeholder')
        self.entry.pack()
        
        self.entry2 = PlaceholderEntry(self.root, placeholder='This text is a ')
        self.entry2.pack()
        self.btn = tk.Button(self.root, text='Nothing', highlightcolor='cyan')
        self.btn.pack()
        

root = tk.Tk()
app = App(master=root)

app.root.mainloop()