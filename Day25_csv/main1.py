import turtle
import pandas as pd


names = []
guessed_states = []

screen = turtle.Screen()
screen.title("State Guessing Name")

image = 'blank_states_img.gif'
screen.addshape(image)
turtle.shape(image)

# def get_mouse_click_coord(x, y):
#     print(x, y)
    
# turtle.onscreenclick(get_mouse_click_coord)

states = pd.read_csv('50_states.csv')
state_col = states.state.to_list()


def add_name(name):
    tim = turtle.Turtle()
    tim.penup()
    tim.hideturtle()
    row = states[states.state == name]
    tim.goto(int(row.x), int(row.y))
    tim.write(f"{name}")
    names.append(tim)

def game_loop():
    guess = screen.textinput("Take a guess", "Guess the state: ")
    if guess == 'exit':
        missed_states = []
        for state in state_col:
            if state not in guessed_states:
                missed_states.append(state)
        
        new_data = pd.DataFrame(missed_states)
        new_data.to_csv('States To Learn.csv')
        
        return False
        
    
    if guess.capitalize() in states.values:
        guessed_states.append(guess.capitalize())
        add_name(guess.capitalize())
        return True
    
while game_loop():
    pass

turtle.exitonclick()