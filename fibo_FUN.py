def fibo_fun(num):
    if num==0:
        return 0
    elif num==1:
        return 1
    else:
        result=fibo_fun(num-2)+fibo_fun(num-1)
        return result
num_of_print=int(input("Please insert the numbers: "))
i=1
while i<num_of_print:
    fibo_val=fibo_fun(i)
    print(fibo_val)
    i+=1
print("ALl Done")


