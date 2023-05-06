'''get_two_digit=input("Please insert two digit")
digit1=int(get_two_digit[0])
digit2=int(get_two_digit[1])
print(digit2+digit1)
your_weight=float(input("Please input your weight\n"))
your_height=float(input("Please input your height\n"))
print(your_weight/(your_height**2))




'''
total_money=float(input('Please input your total money\n'))
total_money_tax=float(input("Please input tax percentage\n"))
people=int(input('Please input your person count\n'))
general_money=total_money*(1+(total_money_tax/100))
money_per_personal="{:.2f}".format((general_money/people))
print( f"Every person should pay  {money_per_personal}  dollars")