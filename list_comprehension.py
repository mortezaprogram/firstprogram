'''
import random
print(list(map((lambda x:x**2),range(1,11))))
print([x**2 for x in range(1,11)])
print(list(filter((lambda x:x%2==0),range(1,11))))
print([x for x in range(1,11) if x%2!=0])
print([x**2 for x in range(50) if (x)%8==0])
print([x*y for x in range(1,10) for y in range(11,20)])
print([x*2 for x in [x*3 for x in range(1,10)] if x%8==0 ])
print([x*3 for x in range(1,10)])
print([x*2 for x in [3, 6, 9, 12, 15, 18, 21, 24, 27]])
print([x for x in [random.randint(1,1000) for x in range(1,51) ] if (x)%9==0])
multi_list=[[1,2,3],[4,5,6],[7,8,9]]
print(multi_list)
print([col[1] for col in multi_list])
print([multi_list[i][i] for i in range(len(multi_list))])

'''
def is_prime(num):
    for i in range(2,num):
        if num%i==0:
            return False
    return True
def gen_prime(max_number):
    for num1 in range(2,max_number):
        if is_prime(num1):
            yield num1
prime=gen_prime(50)
print("Prime: ",next(prime))
print("Prime: ",next(prime))


double=(x*2 for x in range(10))

for y in double:
    print(y)














