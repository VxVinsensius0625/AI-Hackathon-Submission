from tkinter import *
from tkinter import messagebox

root = Tk()
root.title("Custom Message Box")
root.geometry("500x500")


def choice2(option2):# for new group save
    pop3.destroy() # close the pop up window after we choose the options under save tab
    my_label.config(text="You save this tab under new group "+str(option2))

def choice(option): # for existing group save
    pop2.destroy()
    my_label.config(text="You save this tab under group "+str(option))

def existing_group():
    pop.destroy()
    global pop2
    pop2 = Toplevel(root)
    pop2.title("Existing tab options")
    my_frame = Frame(pop2)
    my_frame.pack(pady=5)
    q_label = Label(my_frame, text= "Which group do you want to save this tab ?")
    q_label.grid(row=0,columnspan=5,pady=40)
    global current_group_list 
    current_group_list = [i for i in range(5)]
    for i in current_group_list:
        Button(my_frame,text= str(i), command= lambda k=i: choice(k) ).grid(row = 1, column=i)

# function to create new group tab
def new_group_name():
    pop.destroy()
    global pop3
    pop3 = Toplevel(root)
    pop3.title("New group tab options")
    my_frame = Frame(pop3)
    my_frame.pack(pady=5)
    q_label = Label(my_frame, text= "What is the name of your new group name ?")
    q_label.grid(row=0,columnspan=2,pady=40)
    q_label = Label(my_frame, text= "New Group name: ")
    q_label.grid(row=1,column=0,pady=40)
    e = Entry(my_frame,width=35,borderwidth=5)
    e.grid(row=1,column=1,pady=40)
    #e.insert(0,"New Group name: ")
    ok = Button(my_frame,text = "Submit", command= lambda: choice2(e.get()))
    ok.grid(row=2,columnspan=2,pady=40)


# define pop up window for saving tab options
def clicker():
    global pop # to be able to access the pop up from the main window
    pop = Toplevel(root,bg="#CEF6FF") # new pop up window
    pop.title("Saving tab Options ")
    # e = Entry(pop,width=35,borderwidth=5)
    # e.pack()
    # e.insert(0,"Existing Group:")
    my_frame = Frame(pop,bg="#CEF6FF")
    my_frame.pack(pady=5)
    q_label = Label(my_frame, text= "Where do you want to save this tab ?")
    q_label.grid(row=0,columnspan=2,pady=40)
    old_group = Button(my_frame,text= "Existing group", command= existing_group)
    old_group.grid(row = 1, column= 0,pady=20)
    #old_group.pack(pady=20)
    new_group = Button(my_frame,text = "Make a new group", command= new_group_name)
    new_group.grid(row = 1, column= 1,pady=20)
    #new_group.pack(pady=20)

def no_save_tab():
    global pop4 # to be able to access the pop up from the main window
    pop4 = Toplevel(root,bg="#CEF6FF") # new pop up window
    my_frame = Frame(pop4,bg="#CEF6FF")
    my_frame.pack(pady=5)
    q_label = Label(my_frame, text= "What do you want to do with this tab?")
    q_label.grid(row=0,columnspan=2,pady=40)
    reset_timer = Button(my_frame,text= "Reset Timer", command= None)
    reset_timer.grid(row = 1, column= 0,pady=20)
    delete_cur_tab = Button(my_frame,text= "Delete current tab", command= None)
    delete_cur_tab.grid(row = 1, column= 1,pady=20)



q_label = Label(root, text = "Your Timer has ended. \n Do you want to save the tab?")
q_label.pack(pady=40)

yes_button = Button(root, text = "Yes",command=clicker)
yes_button.pack(pady=40)

no_button = Button(root, text = "No",command=no_save_tab)
no_button.pack(pady=40)

exit_button = Button(root, text = "Exit",command=root.quit)
exit_button.pack(pady=40)

my_label = Label(root,text="")
my_label.pack(pady=20)

root.update()
root.mainloop()