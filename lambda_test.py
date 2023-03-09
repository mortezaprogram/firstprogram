'''
sum1= lambda x,y:x+y
print(sum1(4,7))

can_vote=lambda age:True if age>=10 else False
print(can_vote(50))

power_list=[lambda x:x**2,lambda y:y**3,lambda x:x**4]
for i in power_list:
    print(i(6))

attack={'quick':(lambda:print("quick attack"))
        ,'fast':(lambda :print("fast attack"))
        ,'slow':(lambda:print("slow attack"))}
(attack['quick']())
import random
attack_key=random.choice(list(attack.keys()))

attack[attack_key]()


flip_list=[]
for i in range(1,11):
    flip_list+=random.choice(['H','T'])
print(flip_list)
heads=print(flip_list.count('H'))
tails=print(flip_list.count('T'))

one_to_ten=range(1,11)
def num_multi_2(num):
    return num*2
print(list(map(num_multi_2,one_to_ten)))
print(list(map(lambda x:x*2,one_to_ten)))
b_list=list(map((lambda x,y:x+y),[1,2,3],[4,5,6]))
print(b_list)
print(list(filter((lambda x:x%2==0),range(1,11))))

'''
import random
from functools import reduce
rand_list=list(random.randint(1,1001) for i in range(1,101))
print(list(filter((lambda x:x%9==0),rand_list)))
print(reduce((lambda x,y:x+y),range(1,6)))













