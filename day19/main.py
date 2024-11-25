from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine


menu = Menu()
coffee_maker = CoffeeMaker()
money_machine = MoneyMachine()

#1 Print reports
money_machine.report()
coffee_maker.report()
is_on = True


while is_on:
    options = menu.get_items()
    choice = input(f"What do you want:{options}?\n")
    if choice == "off":
        is_on = False
    elif choice == 'report':
        coffee_maker.report()
        money_machine.report()
    else:
        order = menu.find_drink(choice)
        if coffee_maker.is_resource_sufficient(order) and money_machine.make_payment(order.cost) :
            print("sufficient")
            print(f"Cost is: ${order.cost:.2f}")
            coffee_maker.make_coffee(order)
            money_machine.report()
        else:
            print("Not sufficient")




