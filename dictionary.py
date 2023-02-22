'''my_dictionary={"name":"mori","family_name":"me"}
my_dictionary["city"]="TH"
print("My_dictionary is: ",my_dictionary )
print("Is there any city: ","city"in my_dictionary)
print(my_dictionary.values())
print(my_dictionary.keys())
print(my_dictionary.items())
print(my_dictionary.get("name"))
my_dictionary.clear()
print(my_dictionary)
employees=[]
f_name,l_name=input("Please input f_name and l_name").split()
employees.append({"f_name":f_name,"l_name":l_name})
print(employees)'''
employees= []
while True:
    answer=input("Are you new employee (yes/no):  ")
    if answer=="yes":
        f_name,l_name=input("Please input your first and last name: ").split()
        employees.append({'f_name':f_name,'l_name':l_name})

    else:
        print(employees )
        break
for record in employees:
    print(record['f_name'],record['l_name'])