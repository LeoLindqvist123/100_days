from menu import Menu
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

reporty = CoffeeMaker()

reporty.report()
print(reporty)

left = CoffeeMaker(drink)
left.is_resource_sufficient(drink)
print(left)