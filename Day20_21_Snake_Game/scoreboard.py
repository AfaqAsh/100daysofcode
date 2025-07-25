from turtle import Turtle

class Score(Turtle):
    
    def __init__(self):
        super().__init__()
        self.color("white")
        self.hideturtle()
        self.penup()
        self.goto(0, 280)
        self.write("Score: 1", False, align="center")
        # self.write((0,280), False)
        