'''

'''
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
ws.geometry('500x500')
ws.config(bg='#5FB691')

# e = Entry(ws,width=35,borderwidth=5)
# e.pack()

# define pop up window for saving tab options
def clicker():
    global pop # to be able to access the pop up from the main window
    pop = Toplevel(ws) # new pop up window
    pop.title("Timer Ends ")
    # e = Entry(pop,width=35,borderwidth=5)
    # e.pack()
    # e.insert(0,"Existing Group:")
    my_frame = Frame(pop)
    my_frame.pack(pady=5)
    end_label = Label(my_frame, text= "Your Timer ends")
    end_label.grid(row=0,columnspan=2,pady=40)
    finish_button = Button(my_frame,text= "Done", command= ws.quit)
    finish_button.grid(row = 1, column= 0,pady=20)
    # #old_group.pack(pady=20)
    # new_group = Button(my_frame,text = "Make a new group", command= new_group_name)
    # new_group.grid(row = 1, column= 1,pady=20)
    # #new_group.pack(pady=20)

def timer1(hr, min, s):
    timer_done = countdown(int(hr),int(min),int(s))
    # messagebox.showinfo('Information', timer_done)
    clicker()

q_label = Label(ws, text= "Hour: ")
q_label.grid(row=1,column=0,pady=40)
e1 = Entry(ws,width=35,borderwidth=5)
e1.grid(row=1,column=1,pady=40)

q2_label = Label(ws, text= "Minutes: ")
q2_label.grid(row=2,column=0,pady=40)
e2 = Entry(ws,width=35,borderwidth=5)
e2.grid(row=2,column=1,pady=40)


q3_label = Label(ws, text= "Seconds: ")
q3_label.grid(row=3,column=0,pady=40)
e3 = Entry(ws,width=35,borderwidth=5)
e3.grid(row=3,column=1,pady=40)

mybutton = Button(ws, text='start countdown', command=lambda: timer1( e1.get(),  e2.get(), e3.get()) )
mybutton.grid(row=4,columnspan=3,pady=40)

ws.mainloop()

'''
Reference:
https://www.udacity.com/blog/2021/09/create-a-timer-in-python-step-by-step-guide.html 
'''