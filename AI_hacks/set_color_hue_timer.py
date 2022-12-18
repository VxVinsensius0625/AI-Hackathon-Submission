from tkinter import *
from tkinter import messagebox

root = Tk()
root.title("Color Hue Timer Box")
root.geometry("400x600")

# choices available with user.
time_set = ['Hour','Minute', 'Second']

q_label = Label(root, text = "Color Hue Timer Settings",justify="center")
q_label.grid(row=0,columnspan =3,pady=40)

q_label = Label(root, text = "Red Color",justify="center")
q_label.grid(row=1,column=0,pady=40)

e1 = Entry(root,width=35,borderwidth=5)
e1.grid(row=1,column=1,pady=40)

# setting variable for strings
variable = StringVar()

# set default country as United States
variable.set(time_set[1])
#  creating widget
dropdown = OptionMenu(
    root,
    variable,
    *time_set
)
# positioning widget
dropdown.grid(row=1,column=2,pady=40)

## Second setting
q_label = Label(root, text = "Orange Color",justify="center")
q_label.grid(row=2,column=0,pady=40)

e2 = Entry(root,width=35,borderwidth=5)
e2.grid(row=2,column=1,pady=40)

# setting variable for strings
variable2 = StringVar()

# set default country as United States
variable2.set(time_set[1])
#  creating widget
dropdown2 = OptionMenu(
    root,
    variable2,
    *time_set
)
# positioning widget
dropdown2.grid(row=2,column=2,pady=40)

## Third setting
q_label = Label(root, text = "Green Color",justify="center")
q_label.grid(row=3,column=0,pady=40)

e3 = Entry(root,width=35,borderwidth=5)
e3.grid(row=3,column=1,pady=40)

# setting variable for strings
variable3 = StringVar()

# set default country as United States
variable3.set(time_set[1])
#  creating widget
dropdown3 = OptionMenu(
    root,
    variable3,
    *time_set
)
# positioning widget
dropdown3.grid(row=3,column=2,pady=40)

# Button to set the remainder
set_button = Button(root,text = "Set",command = None)
set_button.grid(row=4,column=0,pady=40)

# Close/remain open tab setting
q_label = Label(root, text = "Auto Close \n Does not delete the history",justify="center")
q_label.grid(row=4,column=1,pady=40)
# choices available with user.
onoff_set = ['On','Off']
# setting variable for strings
variable4 = StringVar()

# set default country as United States
variable4.set(onoff_set[1])
#  creating widget
dropdown4 = OptionMenu(
    root,
    variable4,
    *onoff_set
)
# positioning widget
dropdown4.grid(row=4,column=2,pady=40)

root.mainloop()