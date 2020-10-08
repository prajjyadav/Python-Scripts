import tkinter
from tkinter import BOTH, StringVar, END

#define window
root = tkinter.Tk()
root.title('Hello GUI World!')
root.iconbitmap('wave.ico')
root.geometry("400x400")
root.resizable(0,0)

#define color and fonts
root_color = "#a69cac"
input_color = "#2a9d8f"
output_color = "#d62828"
root.config(bg=root_color)

#define functions
def submit_name():
    if case_style.get() == 'normal':
        name_label = tkinter.Label(output_frame, text="Hello " + name.get(), bg=output_color)
    elif case_style.get() == 'upper':
        name_label = tkinter.Label(output_frame, text=("HELLO " + name.get()).upper(), bg=output_color)
    name_label.pack()
    name.delete(0, END)


#define frames
input_frame = tkinter.LabelFrame(root, bg=input_color)
output_frame = tkinter.LabelFrame(root, bg=output_color)
input_frame.pack(pady=10)
output_frame.pack(padx=10, pady=(0,10), fill=BOTH, expand=True)

#define buttons
name = tkinter.Entry(input_frame, text="Enter your name", width=20)
submit_button = tkinter.Button(input_frame, text="Submit", command=submit_name)
name.grid(row=0, column=0, padx=10, pady=10)
submit_button.grid(row=0, column=1, padx=10, pady=10, ipadx=5)


#create radio buttons
case_style = StringVar()
case_style.set('normal')
normal_button = tkinter.Radiobutton(input_frame, text='Normal Case', variable=case_style, value="normal", bg=input_color)
upper_button = tkinter.Radiobutton(input_frame, text="Upper Case", variable=case_style, value="upper", bg=input_color)
normal_button.grid(row=1, column=0, padx=2, pady=2)
upper_button.grid(row=1, column=1, padx=2, pady=2)
#run the window
root.mainloop()