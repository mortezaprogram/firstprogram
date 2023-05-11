height=1300
age=15
want_photo='Y'
if height >= 120:
    if age<=10:
        bill=100
        # print(f"You have to pay {bill}$ ")
    elif age>=10 and age <= 20:
        bill = 150
        # print(f"You have to pay {bill}$ ")
    elif age > 20:
        bill=200
        # print(f"You have to pay {bill}$ ")
    if want_photo=='Y':
        bill+=10
        print(f"Bill with photo is {bill}$")
    else:
        print(f"Bill with photo is {bill}$")