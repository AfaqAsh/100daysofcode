import random

def choose_difficulty(number_of_tries):
    choice = input('Choose a difficulty. Type easy or hard: ')
    if (choice == 'easy'):
        print('You have 10 tries')
        number_of_tries = 10
    elif (choice == 'hard'):
        print('You have 5 tries')
        number_of_tries = 5
    else:
        print('You did not choose a valid difficulty.')
    
    return number_of_tries

def guess_number(number, number_of_tries):
    while (number_of_tries > 0):
        guess = int(input('Make a guess: '))
        if guess == number:
            print(f'Congratulations. You have correctly guessed the number')
            return
        elif (guess > number):
            print('Too high')
        elif (guess < number):
            print('Too low')
        
        number_of_tries-=1
        print(f'Number of tries left: {number_of_tries}')
            
    
def main_game():
    number_of_tries = 0
    number = random.randint(0, 101)
    print("Guess the number between 1 and 100")
    number_of_tries = choose_difficulty(number_of_tries)
    guess_number(number, number_of_tries)
    
    
main_game()
# outside = 1231

# def inc_out():
#     print(outside)
#     # outside = 32
#     print(outside)

# inc_out()
# print(outside)