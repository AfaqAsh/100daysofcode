from turtle import Turtle

class Scoreboard(Turtle):
    
    def __init__(self):
        super().__init__()
        self.color("white")
        self.penup()
        self.hideturtle()
        self.goto(0, 270)
        self.write(f"0     Score    0", False, align= "center", font=("Arial", 16, "normal"))
        
        
    def update_score(self, lscore, rscore):
        self.clear()
        self.write(f"{lscore}     Score     {rscore}", align= "center", font=("Arial", 16, "normal"))
        