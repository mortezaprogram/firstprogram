'''

def multi_2(num):
    return num*2
my_multi_fun=multi_2
print(my_multi_fun(4))
def do_math(func,num):
    return func(num)
print(do_math(my_multi_fun,2))

def get_multiply(num):
    def multi_ply(value):
       return num*value
    return multi_ply

generated_fun=get_multiply(6)
print(generated_fun(7))


list_of_func=[do_math(my_multi_fun,2),generated_fun(7)]
print(list_of_func)

def is_it_odd(num):
    if (num % 2 == 0):
        return False
    else:
        return True
def change_list(list,func):
    odd_list=[]
    for i in list:
      if func(i):
        odd_list.append(i)
    return odd_list
a_list=range(1,21)
print(change_list(a_list,is_it_odd))
'''
def random_func(name:str,age:int,weight:float)->str:
    print("Name: ",name)
    print("age: ",age)
    print("weight: ",weight)
    return "{} has {} years old and {} weight.".format(name,age,weight)
print(random_func("mori",44,56))
print(random_func.__annotations__)