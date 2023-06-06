# def add(*args):
#     sum=0
#     for n in args:
#         sum+=n
#     return sum

def calculate(n,**kwargs):
    print(kwargs)
    n+=kwargs["add"]
    n*=kwargs["multiply"]
    print(n)
calculate(2,add=100,multiply=2)

class Car:
    def __init__(self,**kw):
        self.make=kw.get("make")
        self.model=kw.get("model")
my_car=Car(make="Nissan",model="GT-R")
print(my_car.model)