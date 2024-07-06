import os

print("Welcome to the secret auction")
quit = False
bidders = {}
while not quit:
    highest_bid = 0
    name = input("What is your name?: ")
    bid = int(input("How much are you bidding?: "))
    cont = input("Are there any other bidders? Type \'yes\' or \'no\': ")
    bidders[name] = bid
    if bid > highest_bid:
        highest_bid = bid
    os.system('cls')
    
    if cont == 'no':
        highest_bidder = {i for i in bidders if bidders[i] == highest_bid}
        print(f'The highest bidder was {highest_bidder} with a bid of {highest_bid}')
        quit = True
        
        