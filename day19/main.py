from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine


menu = Menu()
coffee_maker = CoffeeMaker()
money_machine = MoneyMachine()


user_request = input(f"What do you want:{menu.get_items()}?\n")


#find user request
order = menu.find_drink(user_request)

name = order.name
cost = order.cost
ingredients = order.ingredients

# print(f"Your {name} costs {cost} and requires {ingredients}")


coffee_maker.report()

if coffee_maker.is_resource_sufficient(order):
    print("sufficient")
    coffee_maker.make_coffee(order)
    print(f"Cost is: ${cost:.2f}")
    money_machine.make_payment(cost)
    money_machine.report()

else:
    print("Not sufficient")

