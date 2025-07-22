from turtle import Turtle, Screen

tim = Turtle()

def move_forward():
    tim.forward(10)

def move_backward():
    tim.backward(10)
    
def counter():
    tim.left(10)
    
def clockwise():
    tim.right(10)
    
def clear_screen():
    tim.clear()
    tim.penup()
    tim.home()
    tim.pendown()

screen = Screen()


screen.listen()
screen.onkey(fun=move_forward, key='w')
screen.onkey(fun=move_backward, key='s')
screen.onkey(fun=counter, key='a')
screen.onkey(fun=clockwise, key='d')
screen.onkey(fun=clear_screen, key='c')
screen.exitonclick()



# Higher order function. A function that can work with another function

