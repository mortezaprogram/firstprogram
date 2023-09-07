class Student:
    totalStudent = 0
    def __init__(self, name):
        self.name = name
        Student.totalStudent += 1
        print("Total Students (init) : ", self.totalStudent)

    def __del__(self):
        Student.totalStudent -= 1
        print("Total Students (del) : ", self.totalStudent)

def main():
    s1 = Student("Meher") # Total Students (init) : 1
    s2 = Student("Krishna") # Total Students (init) : 2
    s3 = Student("Patel") # Total Students (init) : 3
## delete object s1
    del s1 # Total Students (del) : 2
# print(s1.name) # error because s1 object is deleted
    print(s2.name) # Krishna
    print(s3.name) # Patel
## since there is no further statements, therefore
## 'del' will be executed for all the objects and
## following results will be displayed
# Total Students (del) : 1
# Total Students (del) : 0
# standard boilerplate to set 'main' as starting function
if __name__=='__main__':
    main()
