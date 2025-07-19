from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

def machine():
    machine_off = False
    order = ''
    coffee_maker = CoffeeMaker()
    menu = Menu()
    counter = MoneyMachine()
    while not machine_off:
        order = input(f"What would you like to order: {menu.get_items()}: ")
        
        if (order == "report"):
            coffee_maker.report()
            counter.report()
        elif (order == "off"):
            machine_off = True
        elif (menu.find_drink(order)):
            item = menu.find_drink(order)
            if (coffee_maker.is_resource_sufficient(item)):
                if counter.make_payment(item.cost):
                    coffee_maker.make_coffee(item)
            else:
                print("Not enough resources.")
        else:
            print("Please input a valid order name.")
            
    
machine()