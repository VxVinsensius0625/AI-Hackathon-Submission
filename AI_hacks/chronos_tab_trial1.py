from tkinter import *
from tkinter import messagebox
import time
import datetime
 
# Create class that acts as a countdown
def countdown(h, m, s):
 
    # Calculate the total number of seconds
    total_seconds = h * 3600 + m * 60 + s
 
    # While loop that checks if total_seconds reaches zero
    # If not zero, decrement total time by one second
    while total_seconds > 0:
 
        # Timer represents time left on countdown
        timer = datetime.timedelta(seconds = total_seconds)

        # Prints the time left on the timer
        #print(timer, end="\r")
        ws.update()
        # Delays the program one second
        time.sleep(1)

        # Reduces total time by one second
        total_seconds -= 1

    return "Bzzzt! The countdown is at zero seconds!"
 
# # Inputs for hours, minutes, seconds on timer
# h = input("Enter the time in hours: ")
# m = input("Enter the time in minutes: ")
# s = input("Enter the time in seconds: ")
# countdown(int(h), int(m), int(s))

ws = Tk()
ws.title('Testing')
ws.geometry('400x200')
ws.config(bg='#5FB691')

e = Entry(ws,width=35,borderwidth=5)
e.pack()


def msg1():
    messagebox.showinfo('information', 'Hi! You got a prompt.')
    messagebox.showerror('error', 'Something went wrong!')
    messagebox.showwarning('warning', 'accept T&C')
    messagebox.askquestion('Ask Question', 'Do you want to continue?')
    messagebox.askokcancel('Ok Cancel', 'Are You sure?')
    messagebox.askyesno('Yes|No', 'Do you want to proceed?')
    messagebox.askretrycancel('retry', 'Failed! want to try again?')


def askMe():
    res = messagebox.askquestion('askquestion', 'Do you want to delete the tab?')
    if res == 'no':
        messagebox.askquestion('Response', 'Where do you want to put the tab?')
    elif res == 'yes':
        messagebox.showinfo('Response', 'You must be a dog fan.')
    else:
        messagebox.showwarning('error', 'Something went wrong!')


def timer1(number):
    num_min = number
    timer_done = countdown(0,int(num_min),0)
    messagebox.showinfo('Information', timer_done)


mybutton = Button(ws, text='start countdown', command=lambda: timer1( e.get() ) ).pack(pady=50)

ws.mainloop()