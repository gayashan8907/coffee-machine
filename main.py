from report import Resources
from process import Money
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
    "water": 400,
    "milk": 300,
    "coffee": 150,}
espresso = MENU['espresso']['ingredients']
cappuccino = MENU['cappuccino']['ingredients']
latte = MENU['latte']['ingredients']
repo = Resources(resources['water'],resources['milk'],resources['coffee'])
def coin_process():
    print('Insert coins')
    quarters = int(input("quarters:"))
    dimes = int(input("dimes:"))
    nickles = int(input('nickles:'))
    pennies = int(input('pennies:'))
    money = Money(quarters, dimes, nickles, pennies, user_choice)
    if money.check_amount():
     return True
    else:
        return False

machine_on = True
while machine_on:
    user_choice= input("What would you like? (espresso/latte/cappuccino):").lower()


    if user_choice == 'report':
        repo.print_report()
    elif user_choice=='latte':
        if repo.enough_resources(latte['water'], latte['milk'], latte['coffee']):
            if coin_process():
                repo.after_make(latte['water'], latte['milk'], latte['coffee'],MENU['latte']['cost'])
        else:
            machine_on=False
    elif user_choice=='espresso':
        if repo.enough_resources(espresso['water'], 0, espresso['coffee']):
            if coin_process():
                repo.after_make(espresso['water'], 0, espresso['coffee'],MENU['espresso']['cost'])
        else:
            machine_on=False
    elif user_choice=='cappuccino':
        if repo.enough_resources(cappuccino['water'], cappuccino['milk'], cappuccino['coffee']):
            if coin_process():
                repo.after_make(cappuccino['water'], cappuccino['milk'], cappuccino['coffee'],MENU['cappuccino']['cost'])
        else:
            machine_on=False




