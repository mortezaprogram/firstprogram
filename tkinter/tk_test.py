import tkinter

window=tkinter.Tk()
window.title("My first GUI Program")
window.minsize(width=300,height=500)
my_label=tkinter.Label(text="It is label", font=("Arial",25,"bold"))
my_label.grid(column=0,row=0)


def button_clicked():
    my_label.config(text=input.get())


button=tkinter.Button(text="Click Me",command=button_clicked)
button.grid(column=1,row=1)
button.config(padx=1,pady=1)

new_button=tkinter.Button(text="Click Me new",command=button_clicked)
new_button.grid(column=2,row=2)
new_button.config(padx=2,pady=2)

input=tkinter.Entry(width=10)
input.grid(column=3,row=3)


window.mainloop()