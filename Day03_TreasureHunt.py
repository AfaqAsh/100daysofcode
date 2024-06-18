print("Welcome to Treasure Island.\nYour job is to find the treasure.\nWhich direction do you want to go, Left or Right?")
first_choice = input("Go Left or Right: ")

if (first_choice.lower() == "left"):
    print("You come across a lake. Do you want to swim across or wait for a boat")
    second_choice = input("Swim or Wait? ")
    if (second_choice.lower() == "wait"):
        print("You took the boat and have arrived at a house with three doors of different color, Red, Yellow, and Blue.\nWhich gate will you enter?")
        third_choice = input("Red, Yellow, or Blue? ")
        if (third_choice.lower() == "red"):
            print("You were burnt by the raging fire inside the door and died.")
        elif (third_choice.lower() == "blue"):
            print("You were attack by the ravenous beasts behind the door and were eaten to death.")
        elif (third_choice.lower() == "yellow"):
            print("You find the treasure and take it all back to become rich.")
        else:
            print("You were killed by a group of passing thieves.")
    else:
        print("You were attacked by a trout while swimming and drowned to your death.")
else:
    print("You fell into a hole after taking the right turn and have died.")
    
# * On the Day03, I did not learn anything new. Just revised the .count() for strings to count the occurence of characters