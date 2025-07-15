import random
from Day14_gamedata import data


def get_personality():
    celeb_a = data[random.randint(0, len(data) - 1)]
    celeb_b = data[random.randint(0, len(data) - 1)]
    return celeb_a, celeb_b
    
def print_celeb(celeb):
    print(f"{celeb['name']}, a {celeb['description']}, from {celeb['country']}")

def compare_guess(celeb_a, celeb_b, guess, score):
    celeb_a_followers = celeb_a['follower_count']
    celeb_b_followers = celeb_b['follower_count']
    correct_answer = 'A'
    if (celeb_a_followers > celeb_b_followers):
        correct_answer = 'A'
    else:
        correct_answer = 'B'
    
    if (guess == correct_answer):
        score += 1
        print(f'You are correct. Your current score is {score}')
        return False, score
    else:
        print(f'You are wrong. Your current score is {score}')
        return True, score
    
    

def main_game():
    score = 0
    quit = False
    while not quit:
        celeb_a, celeb_b = get_personality() 
        print("Compare A: ")
        print_celeb(celeb_a)
        print('VS')
        print("Against B: ")
        print_celeb(celeb_b)
        guess = input('Who has more followers? Type A or B: ')
        quit, score = compare_guess(celeb_a, celeb_b, guess, score)
    
main_game()