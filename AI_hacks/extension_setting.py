from tkinter import *
from tkinter import messagebox
# Menu Settings for the different options

root = Tk()
root.title("Main Settings Box")
root.geometry("500x500")

q_label = Label(root, text = "Main Menu of Chronos Tab Manager ",justify="center")
q_label.grid(row = 0, columnspan=1,pady=40)
#q_label.configure(justify='center')

timer_button = Button(root, text = "Set Timer")
timer_button.grid(row = 1, column=0, pady=40)

color_hue_button = Button(root, text = "Set Color Hue Timer")
color_hue_button.grid(row = 2, column=0, pady=40)

color_hue_button = Button(root, text = "View All Tabs")
color_hue_button.grid(row = 3, column=0, pady=40)
root.mainloop()