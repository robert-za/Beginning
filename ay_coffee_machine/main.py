MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "coffee": 18,
        },
        "cost": 1.5,
    },
    "latte": {
        "ingredients": {
            "water": 200,
            "milk": 150,
            "coffee": 24,
        },
        "cost": 2.5,
    },
    "cappuccino": {
        "ingredients": {
            "water": 250,
            "milk": 100,
            "coffee": 24,
        },
        "cost": 3.0,
    }
}

resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
    "money": 2.5
}


def drink_choice():
    """
    Asks user for a type of coffee and returns the string of coffee
    """
    drink = ''
    while drink not in MENU:
        drink = input("What would you like? espresso/latte/cappuccino: ")
        if drink == "espresso":
            pass
        elif drink == "latte":
            pass
        elif drink == "cappuccino":
            pass
        else:
            print("Sorry, I do not understand.")
    return drink


def check_resources(user_drink, resource, menu):
    """
    Returns boolean: True if enough resources for user_drink and
    False if NOT enough resources for user_drink.
    """
    for drink in MENU:
        if drink == user_drink:
            for ingredient_menu in MENU[drink]["ingredients"]:
                for ingredient_resources in resources:
                    if ingredient_menu == ingredient_resources:
                        if (MENU[drink]["ingredients"][ingredient_menu] <= resources[ingredient_resources]):
                            is_enough_ingredient = True
                            pass
                        else:
                            print(f"Sorry, there is not enough {ingredient_menu} for your {user_drink}.")
                            return False
            return is_enough_ingredient        


def switch_off():
    machine_state = False
    return machine_state


def print_report(resources):
    print(f'Water: {resources["water"]}\nMilk: {resources["milk"]}')
    print(f'Coffee: {resources["coffee"]}\nMoney: {resources["money"]}')


def insert_coins():
    quarters = int(input("quarters: "))
    dimes = int(input("dimes: "))
    nickles = int(input("nickles: "))
    pennies = int(input("pennies: "))
    return round((quarters * 0.25 + dimes * 0.1 + nickles * 0.05 + pennies * 0.01),2)


def check_cash(user_drink, input_sum):
    for drink in MENU:
        if drink == user_drink:
            if MENU[drink]["cost"] == input_sum:
                return True
            elif MENU[drink]["cost"] < input_sum:
                change = input_sum - float(MENU[drink]["cost"])
                print(f"Here is your change: {change}")
                return change
            else:
                print("Not enough money. Your coffee is ${cash}. Add more and try again.")
                return False


def substract_ingredients(user_drink, MENU):
    """
    placeholder
    """
    pass

def return_change(change, resources):
    if isinstance(change, int):
        print(f"Have your {change} back.")
        resources["money"] -= change

    pass


def add_coins_to_machine(change):
    pass

"""
C0DE L0GIC - EXECUTI0N
"""
user_drink = drink_choice()
# print(check_resources(user_drink, resources, MENU))

if check_resources(user_drink, resources, MENU) == True:
    coins_in = insert_coins()

if check_cash(user_drink, coins_in) == True:
    print(f"Here is your {user_drink}")
elif isinstance(check_cash(user_drink, coins_in), int):
    pass

"""
T0-D0:

- offer change [V]

- secret word for switch_off()

- printing report: print_report()

- substract ingredients from resources when transaction is successful

- add coins to the machine

"""

