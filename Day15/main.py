from data import MENU
from data import resources


enough_resources = True
request = ''
while enough_resources and request != 'off':
    request = input("What would you like? (expresso/latte/cappuccino): ").lower()
    if request == 'report':
        print(f"Water: {resources['water']}\nMilk: {resources['milk']}\nCoffee: {resources['coffee']}\nMoney: {resources['money']}")
    elif request in ['espresso','latte','cappuccino']:
        cost = MENU[request]['cost']
        recipe = MENU[request]['ingredients']
        print(cost, recipe)

        # To accept price input and evaluate the price:
        penny = int(input("How may Pennies: ")) * 0.01
        nickel = int(input("How may Nickels: ")) * 0.05
        dime = int(input("How may Dimes: ")) * 0.10
        quarter = int(input("How may Quarters: ")) * 0.25
        pay = sum([penny, nickel, dime, quarter])

        #Go on to make coffee, if we have enough pay

        if pay < cost:
            print("insufficient funds! You have been refunded")
        else:
            if (resources['water'] >= recipe['water']) and resources['milk'] >= recipe['milk'] and resources['coffee'] >= recipe['coffee']:
                #Take from the available resources to make the coffee

                resources['water'] -= recipe['water']
                resources['milk'] -= recipe['milk']
                resources['coffee'] -= recipe['coffee']
                resources['money'] += cost
                print(f"Here's your {request}! and your change: ${round(pay - cost, 2)}")

            else:
                enough_resources = False
                for resource in ['water', 'milk', 'coffee']:
                    if resources[resource] < recipe[resource]:
                        print(f"Sorry there is insufficient {resource}, You will be refunded")

    else: print("Please enter a valid input, or 'report' to check leftover resources and 'off' to shut machine down\nThank You")



