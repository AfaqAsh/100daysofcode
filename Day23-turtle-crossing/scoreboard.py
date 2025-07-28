from turtle import Turtle

FONT = ("Courier", 20, "normal")


class Scoreboard(Turtle):
    
    
    def __init__(self):
        super().__init__()
        self.level = 0
        self.penup()
        self.hideturtle()
        self.goto(-280, 260)
        self.write(f"Level: {self.level}", align= "left", font= FONT)

    def update_level(self):
        self.clear()
        self.level += 1
        self.write(f"Level: {self.level}", align= "left", font= FONT)
        
        
    def game_over(self):
        self.clear()
        self.goto(0,0)
        self.write(f"Game Over\nLevel: {self.level}", align= "center", font= FONT)