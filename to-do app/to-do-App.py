import tkinter
from tkinter import END, ANCHOR


root = tkinter.Tk()
root.title('To-do App')
root.iconbitmap('wave.ico')
root.geometry('500x300')
root.config(bg='#14BDEB')
root.resizable(0,0)

#define functions
def add_item():
    my_listbox.insert(END, list_entry.get())
    list_entry.delete(0, END)

def remove_item():
    my_listbox.delete(ANCHOR)

def clear_list():
    my_listbox.delete(0, END)

def save_list():
    with open('checklist.txt', 'w') as f:
        list_tuple = my_listbox.get(0, END)
        for i in list_tuple:
            if i.endswith('\n'):
                f.write(i)
            else:
                f.write(i + "\n")

def open_list():
    try:
        with open('checklist.txt', 'r') as f:
            for j in f:
                my_listbox.insert(END, j)
    except:
        return
    

#create frames
input_frame = tkinter.Frame(root, bg='#14BDEB')
output_frame = tkinter.Frame(root, bg='#14BDEB')
button_frame = tkinter.Frame(root, bg='#14BDEB')
input_frame.pack()
output_frame.pack()
button_frame.pack()

#create input layout
list_entry = tkinter.Entry(input_frame, borderwidth=3, width=35)
list_add_button = tkinter.Button(input_frame, text='Add', bg="#DCCDE8", borderwidth=3, command=add_item)
list_entry.grid(row=0, column=0, padx=5, pady=5)
list_add_button.grid(row=0, column=1, padx=5, pady=5)

#create output layout
my_scrollbar = tkinter.Scrollbar(output_frame)
my_listbox = tkinter.Listbox(output_frame, width=75,height=14, yscrollcommand=my_scrollbar.set)
my_scrollbar.config(command=my_listbox.yview)
my_listbox.grid(row=0, column=0)
my_scrollbar.grid(row=0, column=1, sticky="NS")

#create button frame
list_remove_button = tkinter.Button(button_frame, text="Remove", bg="#DCCDE8", borderwidth=2, command=remove_item)
list_clear_button = tkinter.Button(button_frame, text="Clear", bg="#DCCDE8", borderwidth=2, command=clear_list)
save_button = tkinter.Button(button_frame, text="Save", bg='#DCCDE8', borderwidth=2, command=save_list)
quit_button = tkinter.Button(button_frame, text="Close", bg="#DCCDE8", borderwidth=2, command=root.destroy)
list_remove_button.grid(row=0, column=0, padx=2, pady=10)
list_clear_button.grid(row=0, column=1, padx=2, pady=10)
save_button.grid(row=0, column=2, padx=2, pady=10)
quit_button.grid(row=0, column=3, padx=2, pady=10)

#define open the backup list
open_list()

root.mainloop()