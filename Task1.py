import tkinter
import random

root = tkinter.Tk()

root.configure(bg='lightyellow')

root.title('To Do Application')

root.geometry('320x250')

no_of_tasks = []




def update_listbox():
    clear_listbox()

    
    for task in no_of_tasks:
        label_task.insert("end", task)

def clear_listbox():
    label_task.delete(0,"end")


def add_task():
    
    task = txt_input.get()
    
    if task != '':
        no_of_tasks.append(task)
        update_listbox()
    else:
        display['text'] = "Please enter a task!"
    txt_input.delete(0,'end')


def delete():
    task = label_task.get('active')
    if task in no_of_tasks:
        no_of_tasks.remove(task)
    
    update_listbox()

    display['text'] = "Task deleted!"

def delete_all():
    global no_of_tasks
    
    no_of_tasks = []

    update_listbox()

def choose_random():
    task = random.choice(no_of_tasks)
    display['text'] = task

def number_of_task():
    number_of_tasks = len(no_of_tasks)

    msg = "Number of tasks : %s" %number_of_tasks
    display['text'] = msg

def exit():
    quit()
    



title = tkinter.Label(root, text = "To-Do-List", bg='lightyellow')
title.grid(row=0,column=0)


display = tkinter.Label(root, text = "", bg='white')
display.grid(row=0,column=1)


txt_input = tkinter.Entry(root, width=15)
txt_input.grid(row=1,column=1)


btn_add_task = tkinter.Button(root, text = "Add Task", fg = 'black', bg = None, command = add_task)

btn_add_task.grid(row=1,column=0)

btn_delete = tkinter.Button(root, text = "Delete", fg = 'black', bg = None, command = delete)

btn_delete.grid(row=2,column=0)


btn_delete_all = tkinter.Button(root, text = "Delete All", fg = 'black', bg = None, command = delete_all)

btn_delete_all.grid(row=3,column=0)


btn_choose_random = tkinter.Button(root, text = "Choose Random", fg = 'black', bg = None, command = choose_random)

btn_choose_random.grid(row=4,column=0)


btn_number_of_task = tkinter.Button(root, text = "Number of Tasks", fg = 'black', bg = None, command = number_of_task)

btn_number_of_task.grid(row=5,column=0)


btn_close = tkinter.Button(root, text = "Exit", fg = 'black', bg = None, command = exit)

btn_close.grid(row=6,column=0)


label_task = tkinter.Listbox(root)
label_task.grid(row=2,column=1,rowspan=7)



root.mainloop()