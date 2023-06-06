import tkinter
window=tkinter.Tk()
window.title("Mile to KiloMeter Program")
window.minsize(width=180,height=50)
window.config(padx=20,pady=20)
my_label=tkinter.Label(text="is equal to", font=("Arial",10,"bold"))
my_label.grid(column=0,row=1)
my_label_2=tkinter.Label(text="Miles", font=("Arial",10,"bold"))
my_label_2.grid(column=2,row=0)
my_label_3=tkinter.Label(text="Km", font=("Arial",10,"bold"))
my_label_3.grid(column=2,row=1)


def mile_to_km():
    mile=float(input.get())
    km=(1.609*mile)
    my_label_4.config(text=f"{km}")


button=tkinter.Button(text="Convert",command=mile_to_km)
button.grid(column=1,row=2)
input=tkinter.Entry(width=10)
input.grid(column=1,row=0)
my_label_4=tkinter.Label(text="0", font=("Arial",10,"bold"))
my_label_4.grid(column=1,row=1)

window.mainloop()