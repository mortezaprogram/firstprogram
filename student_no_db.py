from tkinter import *
from tkinter import ttk
class StudentDB:
    headers = ['ID', 'First Name', 'Last Name', 'Email', 'Street', 'City', 'State', 'Zip', 'Phone','Birth', 'Sex', 'Lunch']
    student_info = [
        (1, 'Dale', 'Cooper', 'dcooper@aol.com', '123 Main St', 'Yakima', 'WA', 98901,
         '792-223-8901', '1959-2-22', 'M', 3.50),
        (2, 'Harry', 'Truman', 'htruman@aol.com', '202 South St', 'Vancouver', 'WA', 98660,
         '792-223-9810', '1946-1-24', 'M', 3.50),
        (3, 'Shelly', 'Johnson', 'sjohnson@aol.com', '9 Pond Rd', 'Sparks', 'NV', 89431,
         '792-223-6734', '1970-12-12', 'F', 3.50),
        (3, 'Shelly', 'Johnson', 'sjohnson@aol.com', '9 Pond Rd', 'Sparks', 'NV', 89431,
         '792-223-6734', '1970-12-12', 'F', 3.50),
        (3, 'Shelly', 'Johnson', 'sjohnson@aol.com', '9 Pond Rd', 'Sparks', 'NV', 89431,
         '792-223-6734', '1970-12-12', 'F', 3.50),
        (3, 'Shelly', 'Johnson', 'sjohnson@aol.com', '9 Pond Rd', 'Sparks', 'NV', 89431,
         '792-223-6734', '1970-12-12', 'F', 3.50),
        (3, 'Shelly', 'Johnson', 'sjohnson@aol.com', '9 Pond Rd', 'Sparks', 'NV', 89431,
         '792-223-6734', '1970-12-12', 'F', 3.50),
        (3, 'Shelly', 'Johnson', 'sjohnson@aol.com', '9 Pond Rd', 'Sparks', 'NV', 89431,
         '792-223-6734', '1970-12-12', 'F', 3.50),
        (3, 'Shelly', 'Johnson', 'sjohnson@aol.com', '9 Pond Rd', 'Sparks', 'NV', 89431,
         '792-223-6734', '1970-12-12', 'F', 3.50),
        (3, 'Shelly', 'Johnson', 'sjohnson@aol.com', '9 Pond Rd', 'Sparks', 'NV', 89431,
         '792-223-6734', '1970-12-12', 'F', 3.50),
        (3, 'Shelly', 'Johnson', 'sjohnson@aol.com', '9 Pond Rd', 'Sparks', 'NV', 89431,
         '792-223-6734', '1970-12-12', 'F', 3.50),
        (3, 'Shelly', 'Johnson', 'sjohnson@aol.com', '9 Pond Rd', 'Sparks', 'NV', 89431,
         '792-223-6734', '1970-12-12', 'F', 3.50),
        (3, 'Shelly', 'Johnson', 'sjohnson@aol.com', '9 Pond Rd', 'Sparks', 'NV', 89431,
         '792-223-6734', '1970-12-12', 'F', 3.50),
        (3, 'Shelly', 'Johnson', 'sjohnson@aol.com', '9 Pond Rd', 'Sparks', 'NV', 89431,
         '792-223-6734', '1970-12-12', 'F', 3.50),
        (3, 'Shelly', 'Johnson', 'sjohnson@aol.com', '9 Pond Rd', 'Sparks', 'NV', 89431,
         '792-223-6734', '1970-12-12', 'F', 3.50),
        (3, 'Shelly', 'Johnson', 'sjohnson@aol.com', '9 Pond Rd', 'Sparks', 'NV', 89431,
         '792-223-6734', '1970-12-12', 'F', 3.50),
        (3, 'Shelly', 'Johnson', 'sjohnson@aol.com', '9 Pond Rd', 'Sparks', 'NV', 89431,
         '792-223-6734', '1970-12-12', 'F', 3.50)
    ]
    def __init__(self):
        self.tree = None
        self.create_widgets()

    def create_widgets(self):
        sid_label = Label(root, text='ID')
        sid_label.grid(row=0, column=0, padx=5, pady=10, sticky=W)
        self.sid_entry_value = StringVar(root, value="")
        self.sid_entry = ttk.Entry(root,textvariable=self.sid_entry_value)
        self.sid_entry.grid(row=0, column=1, padx=5, pady=10, sticky=W)
        f_name_label = Label(root, text='First Name')
        f_name_label.grid(row=0, column=2, padx=5, pady=10, sticky=W)
        self.f_name_entry_value = StringVar(root, value="")
        self.f_name_entry = ttk.Entry(root,textvariable=self.f_name_entry_value)
        self.f_name_entry.grid(row=0, column=3, padx=5, pady=10, sticky=W)
        l_name_label = Label(root, text='Last Name')
        l_name_label.grid(row=0, column=4, padx=5, pady=10, sticky=W)
        self.l_name_entry_value = StringVar(root, value="")
        self.l_name_entry = ttk.Entry(root,textvariable=self.l_name_entry_value)
        self.l_name_entry.grid(row=0, column=5, padx=5, pady=10, sticky=W)
        email_label = Label(root, text='Email')
        email_label.grid(row=0, column=6, padx=5, pady=10, sticky=W)
        self.email_entry_value = StringVar(root, value="")
        self.email_entry = ttk.Entry(root,textvariable=self.email_entry_value)
        self.email_entry.grid(row=0, column=7, padx=5, pady=10, sticky=W)
        street_label = Label(root, text='Street')
        street_label.grid(row=0, column=8, padx=5, pady=10, sticky=W)
        self.street_entry_value = StringVar(root, value="")
        self.street_entry = ttk.Entry(root,textvariable=self.street_entry_value)
        self.street_entry.grid(row=0, column=9, padx=5, pady=10, sticky=W)
        city_label = Label(root, text='City')
        city_label.grid(row=1, column=0, padx=5, pady=10, sticky=W)
        self.city_entry_value = StringVar(root, value="")
        self.city_entry = ttk.Entry(root,textvariable=self.city_entry_value)
        self.city_entry.grid(row=1, column=1, padx=5, pady=10, sticky=W)
        state_label = Label(root, text='State')
        state_label.grid(row=1, column=2, padx=5, pady=10, sticky=W)
        self.state_entry_value = StringVar(root, value="")
        self.state_entry = ttk.Entry(root,textvariable=self.state_entry_value)
        self.state_entry.grid(row=1, column=3, padx=5, pady=10, sticky=W)
        zip_label = Label(root, text='Zip Code')
        zip_label.grid(row=1, column=4, padx=5, pady=10, sticky=W)
        self.zip_entry_value = StringVar(root, value="")
        self.zip_entry = ttk.Entry(root,textvariable=self.zip_entry_value)
        self.zip_entry.grid(row=1, column=5, padx=5, pady=10, sticky=W)
        phone_label = Label(root, text='Phone')
        phone_label.grid(row=1, column=6, padx=5, pady=10, sticky=W)
        self.phone_entry_value = StringVar(root, value="")
        self.phone_entry = ttk.Entry(root,textvariable=self.phone_entry_value)
        self.phone_entry.grid(row=1, column=7, padx=5, pady=10, sticky=W)
        birth_label = Label(root, text='Birth')
        birth_label.grid(row=1, column=8, padx=5, pady=10, sticky=W)
        self.birth_entry_value = StringVar(root, value="")
        self.birth_entry = ttk.Entry(root,textvariable=self.birth_entry_value)
        self.birth_entry.grid(row=1, column=9, padx=5, pady=10, sticky=W)
        sex_label = Label(root, text='Sex')
        sex_label.grid(row=2, column=0, padx=5, pady=10, sticky=W)
        self.sex_entry_value = StringVar(root, value="")
        self.sex_entry = ttk.Entry(root,textvariable=self.sex_entry_value)
        self.sex_entry.grid(row=2, column=1, padx=5, pady=10, sticky=W)
        lunch_label = Label(root, text='Lunch')
        lunch_label.grid(row=2, column=2, padx=5, pady=10, sticky=W)
        self.lunch_entry_value = StringVar(root, value="")
        self.lunch_entry = ttk.Entry(root,textvariable=self.lunch_entry_value)
        self.lunch_entry.grid(row=2, column=3, padx=5, pady=10, sticky=W)

        add_button = ttk.Button(root, text='Add Student', command=self.add_student)
        add_button.grid(column=4, row=2, sticky=(W, E))
        update_button = ttk.Button(root, text='Update Student', command=self.update_student)
        update_button.grid(column=5, row=2, sticky=(W, E))
        delete_button = ttk.Button(root, text='Delete Student', command=self.delete_student)
        delete_button.grid(column=6, row=2, sticky=(W, E))

        self.tree = ttk.Treeview(root, height=15, columns=('ID', 'First Name', 'Last Name', 'Email','Street', 'City', 'State', 'Zip', 'Phone', 'Birth', 'Sex','Lunch'), selectmode='browse')
        self.tree.grid(row=3, column=0, columnspan=17)
        self.tree['show'] = 'headings'
        i = 1
        for col in self.headers:
            num = f'#{i}'
        self.tree.heading(num, text=col)
        self.tree.column(num, width=115)
        i += 1

        for stud_info in self.student_info:
            num = f'#{i}'
        self.tree.insert('', 'end', values=stud_info)
        i += 1

    def add_student(self):
            pass

    def update_student(self):
            pass

    def delete_student(self):
            pass

root = Tk()
root.geometry("1400x600")
root.title("Student Database")
student_db = StudentDB()
root.mainloop()

