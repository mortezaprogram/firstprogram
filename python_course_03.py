print("*********************************************************** ")
print("**************** Welcome to Pizza delivery **************** ")
print("*********************************************************** \n")
size=input("Please input the pizza size(S,M,L)\n")
pep=input("Do you need pepperoni (Y,N) \n")
cheese=input("Do you need cheese (Y,N)\n ")
bill=0
if size=="S":
     bill=10
elif size=="M":
     bill=20
elif size == "M":
     bill = 30
if pep=="Y":
    if size=="S" or size=="M" :
        bill+=1
    else:
        bill+=2
if cheese=="Y":
    bill+=5
print(f"Your final bill is {bill}$")
