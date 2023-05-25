from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine
menu=Menu()
is_on=True
money_machine=MoneyMachine()
coffee_maker=CoffeeMaker()



while is_on:
    choice=menu.get_items()
    choice=input(f"Please inter your option: ({choice})")
    if choice=="off":
        is_on=False
    elif choice=="report":
        print(coffee_maker.report())
        print(money_machine.report())
    else:
        drink=menu.find_drink(choice)
        if coffee_maker.is_resource_sufficient(drink) and money_machine.make_payment(drink.cost):
            coffee_maker.make_coffee(drink)
