'''try:
   mylist=[1,2,3]
   print(mylist)
except IndexError:
    print("There is an index error")
except:
    print("Some thing is going wrong")
class DogNameError(Exception):
    def __init__(self,*args,**kwargs):
        Exception.__init__(self,*args,**kwargs)
try:
    dog_name=input("Please input your dog name: ")
    if any(char.isdigit() for char in dog_name):
        raise DogNameError
except DogNameError:
    print("You can not input a digit in dog name")

num1,num2=input("Please input two number for division: ").split()
try:
    division_result=int(num1)/int(num2)
    print("{}/{}={}".format(num1,num2,division_result))
except ZeroDivisionError:
    print("The second number can't be zero")
finally:
    print("There isn't any problem")
'''
try:
    my_file=open("mydata.txt",encoding="utf-8")
except FileNotFoundError as ex:
    print("The file can not find")
    print(ex.args)
else:
    print('My_file: ',my_file.read())
    my_file.close()
finally:
    print("finished working with file")