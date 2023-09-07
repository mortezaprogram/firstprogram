arr=[10,20,30]
for i in range(len(arr)):
    b=arr[i]*2
    print(b)

for a,i in enumerate((arr)):
     print(i,a)

dc = { 'Toy':3, 'Play':4, 'Games':5}
for i,j in dc.items():
    print(i,j)

k = ['Toy', 'Game', 'Tiger']
v = ['Toys', 'Games', 'Tigers']
dc=dict(zip(k,v))
print(dc)

d=dict(enumerate(v))
print(d)



animals = ['tiger', 'cat', 'dog']
am = animals.copy()
print(am)

animals = ['tiger', 'cat', 'dog']
for a in animals[:]:
    if len(a) > 3:
        animals.append(a)
print(animals)


def testnumber(num):
    if num in [1,3]:
        print("OK")
    else:
        print("Not OK")
print(testnumber(3))

student = ["Tom", 90, 95, 98, 30]
Name, *Marks, Age = student
print(Name,Marks,Age)


y = (1, "Two", 3, ("Five", "Six", "Seven"))
a, *b, (*c, d) = y
print(a,b,c,d)