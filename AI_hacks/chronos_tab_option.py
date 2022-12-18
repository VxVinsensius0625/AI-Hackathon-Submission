from tkinter import *
from tkinter import messagebox
def messageWindow():
    win = Toplevel()
    win.title('warning')
    message = "This will delete stuff"
    Label(win, text=message).pack()
    Button(win, text='Delete', command=None).pack()


ws = Tk()
ws.title('Chronos Tab option Testing')
ws.geometry('400x200')
ws.config(bg='#5FB691')
mybutton = Label(ws, text='Option',pady=10 ).pack()
mybutton2 = Button(ws, text='Option2', command= messageWindow , pady=10).pack()

ws.mainloop()