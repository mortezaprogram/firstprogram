from tkinter import *
import tkinter.filedialog
import ast
class TextEditor:
    @staticmethod
    def quit_app(event=None):
        root.quit()
    def remake_file(self,text_area_list):
        for i in text_area_list:
            print("Key",i[0])
            print("Value",i[1])
            print("Index",i[2])
    def open_file(self,event=None):
        txt_file=tkinter.filedialog.askopenfilename(parent=root,initialdir="/")
        if txt_file:
            self.text_area.delete(1.0,END)
            file_list=[]
            with open(txt_file) as _file:
                file_list=list(ast.literal_eval(_file.read()))
                print(file_list)
                for data in file_list:
                    if data[0] == "text":
                        self.text_area.insert(data[2], data[1])
                i=0
                while i < len(file_list):
                    if (file_list[i][0] == "tagon") and (file_list[i][1]!="sel"):
                        styling=file_list[i][1]
                        start_of_style=file_list[i][2]
                        end_of_style=END
                        if (i + 4) < len(file_list):
                            end_of_style = file_list[i + 4][2]
                        print("Style", styling)
                        print("Start", start_of_style)
                        print("End", end_of_style)
                        self.text_area.tag_add(styling,start_of_style,end_of_style)
                    i += 1
                root.update_idletasks()

    def save_file(self, event=None):
        file = tkinter.filedialog.asksaveasfile(mode='w')
        if file is not None:
            data = self.text_area.get('1.0', END + '-1c')
            text_area_list=self.text_area.dump('1.0', END + '-1c')
            file.write(''.join('("{}","{}","{}"),'.format(x[0],x[1],x[2]) for x in text_area_list))
            file.close()

    def make_bold(self):
        self.text_area.tag_add("bt", "sel.first", "sel.last")

    def __init__(self, root):
        self.text_to_write = ""
        root.title("Text Editor")
        root.geometry("600x550")
        frame = Frame(root, width=600, height=550)
        scrollbar = Scrollbar(frame)
        self.text_area = Text(frame, width=600, height=550, yscrollcommand=scrollbar.set, padx=10, pady=10,
                              font=("Georgia", "28"))
        scrollbar.config(command=self.text_area.yview)
        scrollbar.pack(side="right", fill="y")
        self.text_area.pack(side="left", fill="both", expand=True)
        frame.pack()
        file_menu = Menu(the_menu, tearoff=0)
        file_menu.add_command(label="Open", command=self.open_file)
        file_menu.add_command(label="Save", command=self.save_file)
        file_menu.add_separator()
        file_menu.add_command(label="Quit", command=self.quit_app)
        the_menu.add_cascade(label="File", menu=file_menu)
        edit_menu = Menu(the_menu, tearoff=0)
        edit_menu.add_command(label="Bold", command=self.make_bold)
        the_menu.add_cascade(label="Edit", menu=edit_menu)
        self.text_area.tag_config("bt", font=("Georgia", "28", "bold"))
        root.config(menu=the_menu)

root = Tk()
the_menu = Menu(root)
text_editor = TextEditor(root)
root.mainloop()
