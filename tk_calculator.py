from tkinter import *
from tkinter import ttk
class Calculator:
    calc_value=0.0
    div_trigger=False
    mult_trigger=False
    add_trigger=False
    sub_trigger=False
    def button_pressed(self,value):
        if value=='AC':
            self.div_trigger = False
            self.mult_trigger = False
            self.add_trigger = False
            self.sub_trigger = False
            self.number_entry.delete(0,"end")
            entry_val=0
            self.number_entry.insert(0, entry_val)
        else:
            entry_val=self.number_entry.get()
            entry_val+=value
            self.number_entry.delete(0,"end")
            self.number_entry.insert(0,entry_val)
    def isfloat(self,str_val):
        try:
            float(str_val)
            return True
        except ValueError:
            return False
    def math_button_press(self,value):
        if self.isfloat(str(self.number_entry.get())):
            self.div_trigger = False
            self.mult_trigger = False
            self.add_trigger = False
            self.sub_trigger = False
            self.calc_value=float(self.entry_value.get())
            if value=="/":
                print("/ Pressed")
                self.div_trigger=True
            elif value=="*":
                print("* Pressed")
                self.mult_trigger=True
            elif value=="+":
                print("+ Pressed")
                self.add_trigger=True
            else:
                print("- Pressed")
                self.sub_trigger=True
            self.number_entry.delete(0,"end")
    def equal_button_pressed(self):
        if self.add_trigger or self.sub_trigger or self.mult_trigger or self.div_trigger:
            if self.add_trigger:
              solution = self.calc_value + float(self.entry_value.get())

            elif self.sub_trigger:
              solution = self.calc_value - float(self.entry_value.get())
            elif self.mult_trigger:
              solution = self.calc_value * float(self.entry_value.get())
            else:
              solution = self.calc_value / float(self.entry_value.get())
            print(self.calc_value, " ", float(self.entry_value.get())," ", solution)
            self.number_entry.delete(0, "end")
            self.number_entry.insert(0,solution)
    def __init__(self,root):
       self.entry_value=StringVar(root,value="")
       root.title("Calculator")
       #483x220
       root.geometry("590x240")
       root.resizable(width=False,height=False)
       style=ttk.Style()
       style.configure("TButton",font="Serif 15",padding=10)
       style.configure("TEntry",font="Serif 18",padding=10)
       self.number_entry=ttk.Entry(root,textvariable=self.entry_value,width=50)
       self.number_entry.grid(columnspan=4,row=0,sticky=(W,E))

       self.button7=ttk.Button(root,text="7",command=lambda:self.button_pressed('7')).grid(column=0,row=1,sticky=(W,E))
       self.button8=ttk.Button(root,text="8",command=lambda:self.button_pressed('8')).grid(column=1,row=1,sticky=(W,E))
       self.button9=ttk.Button(root,text="9",command=lambda:self.button_pressed('9')).grid(column=2,row=1,sticky=(W,E))
       self.button_div=ttk.Button(root,text="/",command=lambda:self.math_button_press('/')).grid(column=3,row=1,sticky=(W,E))

       self.button4 = ttk.Button(root, text="4",command=lambda:self.button_pressed('4')).grid(row=2, column=0, sticky=(W, E))
       self.button5 = ttk.Button(root, text="5",command=lambda:self.button_pressed('5')).grid(row=2, column=1, sticky=(W, E))
       self.button6 = ttk.Button(root, text="6",command=lambda:self.button_pressed('6')).grid(row=2, column=2, sticky=(W, E))
       self.button_mult = ttk.Button(root, text="*",command=lambda:self.math_button_press('*')).grid(row=2, column=3, sticky=(W, E))

       self.button1 = ttk.Button(root, text="1",command=lambda:self.button_pressed('1')).grid(row=3, column=0, sticky=(W, E))
       self.button2 = ttk.Button(root, text="2",command=lambda:self.button_pressed('2')).grid(row=3, column=1, sticky=(W, E))
       self.button3 = ttk.Button(root, text="3",command=lambda:self.button_pressed('3')).grid(row=3, column=2, sticky=(W, E))
       self.button_add = ttk.Button(root, text="+",command=lambda:self.math_button_press('+')).grid(row=3, column=3, sticky=(W, E))

       self.button_clear = ttk.Button(root, text="AC",command=lambda:self.button_pressed('AC')).grid(row=4, column=0, sticky=(W, E))
       self.button0 = ttk.Button(root, text="0",command=lambda:self.button_pressed('0')).grid(row=4, column=1, sticky=(W, E))
       self.button_equal = ttk.Button(root, text="=",command=lambda:self.equal_button_pressed()).grid(row=4, column=2, sticky=(W, E))
       self.button_sub = ttk.Button(root, text="-",command=lambda:self.math_button_press('-')).grid(row=4, column=3, sticky=(W, E))

root=Tk()
calc=Calculator(root)
root.mainloop()