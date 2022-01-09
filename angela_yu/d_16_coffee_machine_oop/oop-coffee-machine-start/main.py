from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

print("coffee machine!")

is_on = True
coffee_choices = Menu()
coffee_maker = CoffeeMaker()
money_machine = MoneyMachine()

while is_on:
    choice = input(f"What would you like? {coffee_choices.get_items()}")
    if choice in coffee_choices.get_items():
        user_drink = coffee_choices.find_drink(choice)
        if coffee_maker.is_resource_sufficient(user_drink) and money_machine.make_payment(user_drink.cost):
            coffee_maker.make_coffee(user_drink)
    elif choice == "ireport":
        coffee_maker.report()
    elif choice == "mreport":
        money_machine.report()
    elif choice == "report":
        coffee_maker.report()
        money_machine.report()
    elif choice == "off":
        is_on = False