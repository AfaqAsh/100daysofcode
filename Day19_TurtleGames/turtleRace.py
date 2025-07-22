from turtle import Turtle, Screen
import random

screen = Screen()
screen.setup(width=500, height=400)
player_choice = screen.textinput("Turtle Race", "Which turtle do you wanna bid on?: " )
turtles = []
colors = ["red", "blue", "green", "black", "purple", "orange"]

y = -150
for i in range(6):
    turtle = Turtle()
    turtle.penup()
    turtle.shape("turtle")
    turtle.color(random.choice(colors))
    turtle.goto(-240, y)
    y += 50
    turtles.append(turtle)
   
def race_turtles():
    quit_race = False
    while not quit_race:
        for turtle in turtles:
            turtle.forward(random.randint(0,10))
            position = turtle.pos()[0]
            if position >= 230.0:
                winning_turtle = turtle.color()[0]
                print(f"Winner {winning_turtle}")  
                if (player_choice == winning_turtle):
                    print("You won") 
                quit_race = True
# print(turtles[0].pos())  


race_turtles()
screen.exitonclick()