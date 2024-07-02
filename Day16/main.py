#import turtle
import another_module
#print(another_module.another_variable)


# from turtle import *
# timmy = Turtle()
# my_screen = Screen()
# timmy.shape("turtle")
# timmy.color("coral")
# timmy.forward(20)
# timmy.forward(20)
# #timmy.forward(20)
# print(my_screen.canvheight)
# my_screen.exitonclick()


# import prettytable
# table = prettytable.PrettyTable()
#
# table.add_column("Name", ['Adenubi', 'Oreofe', 'Moses'])
# table.add_column("Abbrv.", ['Adnbi', 'Orfe', 'Mses'])
# table.align = 'l'
#
# print(table)


from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

menu = Menu()
coffee_machine = CoffeeMaker()
money_machine = MoneyMachine()
while True:
    order = input("Welcome to the coffee Machine, pick a drink (espresso/latte/cappuccino) or 'off' to shut down: ").lower()
    if order == 'off':
        break

    order = menu.find_drink(order)
    if order.name in menu.get_items() and coffee_machine.is_resource_sufficient(order): # is Drink available? and
        cost = order.cost # Obtain the cost of drink                                       do we have enough resources
        print(f"Drink will cost ${cost}")

        if money_machine.make_payment(cost):
            coffee_machine.make_coffee(order)

    else:
        print("Please enter a valid drink or 'Off' to shut down.")