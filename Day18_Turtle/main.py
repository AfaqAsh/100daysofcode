import turtle as t
from random import randint, choice

tim = t.Turtle()
tim.shape('turtle')
tim.color('PaleGreen')
t.colormode(255)

# Draw a square
def draw_square():
    for _ in range(4):
        tim.forward(100)
        tim.right(90)
    
# Draw a dashed line
def draw_dashed():
    for _ in range(10):
        tim.pendown()
        tim.forward(10)
        tim.penup()
        tim.forward(10)
    tim.pendown()

# Draw a polygon
def draw_shape(sides):
    exterior = 360 / sides
    for _ in range(sides):
        tim.forward(100)
        tim.right(exterior)
  
#Random Walk      
def random_walk():
    tim.pen(speed=10)
    direction = [0, 90, 180, 270]
    tim.width(10)
    for _ in range(100):
        tim.forward(50)
        tim.left(choice(direction))
        tim.color(random_color())
    

def random_color():
    r = randint(0, 255)
    g = randint(0, 255)
    b = randint(0, 255)
    return (r, g, b)

# print(random_color())
# random_walk()
# draw_dashed()
# draw_square()


# for i in range(3, 11):
#     draw_shape(i)
#     tim.color(random_color())

def draw_spirograph(steps):
    tim.speed("fastest")
    for i in range(int(360 / steps)):
        tim.circle(100)
        tim.left(steps)
        tim.color(random_color())


draw_spirograph(1)





screen = t.Screen()
screen.exitonclick()