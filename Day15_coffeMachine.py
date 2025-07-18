def get_order():
    order = input("What would you like to have? (espresso/latte/cappuccino): ")
    return order

def show_resources(water, milk, coffee, money):
    print(f"Water is {water}ml \nMilk is {milk}ml \nCoffee is {coffee}g \nMoney is ${money}")
    
def insert_coins():
    quarters = int(input('How many quarters?: '))
    dimes = int(input('How many dimes?: '))
    nickles = int(input('How many nickels?: '))
    pennies = int(input('How many pennies?: '))
    
    pennies = pennies * 0.01
    nickles = nickles * 0.05
    dimes = dimes * 0.10
    quarters = quarters * 0.25
    total_money = pennies + nickles + dimes + quarters
    return total_money
    

def make_espresso(water, coffee, balance):
    req_water = 50
    req_coffee = 18
    req_money = 1.50
    if (water >= req_water and coffee >= req_coffee):
        inserted_money = insert_coins()
        if inserted_money >= req_money:
            water = water - req_water
            coffee = coffee - req_coffee
            balance = balance + req_money
            print(f"Here is your espresso and your change {inserted_money - req_money}")
        else:
            print("Not enough money")
    else:
        print("Sorry, the machine does not has enough resources for your order")
    
    return water, coffee, balance
    
    
def make_latte(water, coffee, milk, balance):
    req_water = 200
    req_coffee = 24
    req_milk = 150
    req_money = 2.50
    if (water >= req_water and coffee >= req_coffee and milk >= req_milk):
        inserted_money = insert_coins()
        if inserted_money >= req_money:
            water = water - req_water
            coffee = coffee - req_coffee
            milk = milk - req_milk
            balance = balance + req_money
            print(f"Here is your Latte and your change {inserted_money - req_money}")
        else:
            print("Not enough money")
    else:
        print("Sorry, the machine does not has enough resources for your order")
    
    return water, coffee, milk, balance

def make_cap(water, coffee, milk, balance):
    req_water = 250
    req_coffee = 24
    req_milk = 100
    req_money = 3.00
    if (water >= req_water and coffee >= req_coffee and milk >= req_milk):
        inserted_money = insert_coins()
        if inserted_money >= req_money:
            water = water - req_water
            coffee = coffee - req_coffee
            milk = milk - req_milk
            balance = balance + req_money
            print(f"Here is your Cappuccino and your change {inserted_money - req_money}")
        else:
            print("Not enough money")
    else:
        print("Sorry, the machine does not has enough resources for your order")
    
    return water, coffee, milk, balance


def main_machine():
    water = 300
    milk = 200
    coffee = 100
    balance = 0.0
    
    machine_turned_off = False
    while not machine_turned_off:
        order = get_order()
        if order == 'off':
            machine_turned_off = True
        elif order == "report":
            show_resources(water, milk, coffee, balance)
        elif order == 'espresso':
            water, coffee, balance = make_espresso(water, coffee, balance)
        elif order == 'latte':
            water, coffee, milk, balance = make_latte(water, coffee, milk, balance)
        elif order == 'cappuccino':
            water, coffee, milk, balance = make_cap(water, coffee, milk, balance)
        else:
            print("Enter valid command")
        

main_machine()