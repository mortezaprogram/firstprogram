class StudentID:
    def __init__(self,id,name,age="30"):
        self.id=id
        self.name=name
        self.age=age

    def __setattr__(self, name, value):
        if (name == "id"):
            if isinstance(value, int) and value > 0:
                self.__dict__["id"] = value
            else:
                raise TypeError("Id must be positive integer")
        elif (name == "firstName"):
            self.__dict__["firstName"] = value
        else:
            self.__dict__[name] = value
    def __getattr__(self, name):
         raise AttributeError("Attribute does not exist")

def main():
    s1 = StudentID(1, "Meher",66)
    print(s1.id, s1.name, s1.age)
    # s2 = StudentID(-1, "Krishna", 28)
    s3 = StudentID(2, "Krishna", 28)
    print(s3.id, s3.firstName, s3.age)

if __name__=='__main__':
    main()