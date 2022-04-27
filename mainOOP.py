from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine
power = 'on'
menu = Menu()
coffee_machine = CoffeeMaker()
money = MoneyMachine()
# options = menu.get_items()
while power == 'on':
    user_input = input(f"What would you like ({menu.get_items()})?")
    if user_input == 'off':
        power = 'off'
        exit('powering off...')
    elif user_input == 'report':
        coffee_machine.report()
        money.report()
    elif menu.find_drink(user_input) is not None:
        drink = menu.find_drink(user_input)
        print(user_input)
        if coffee_machine.is_resource_sufficient(drink) is True:
            print(f'cost: ${drink.cost}')
            if money.make_payment(drink.cost) is True:
                coffee_machine.make_coffee(drink)



