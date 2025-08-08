from turtle import Turtle

class Score(Turtle):
    
    def __init__(self):
        super().__init__()
        self.score = 0
        with open("high_score.txt", mode="r") as file:
            high_score = int(file.read())
            self.high_score = high_score
        self.color("white")
        self.hideturtle()
        self.penup()
        self.goto(0, 280)
        self.write(f"Score: {self.score}  High Score: {self.high_score}", False, align="center", font=('Arial', 12, 'normal'))
        
        
    def add_score(self):
        self.score += 1
        self.clear()
        self.write(f"Score: {self.score}  High Score: {self.high_score}", False, align="center", font=('Arial', 12, 'normal'))
        
    def game_over(self):
        if self.score > self.high_score:
            self.high_score = self.score
            with open("high_score.txt", mode="w") as file:
                file.write(str(self.high_score))
        self.score = 0
        self.clear()
        self.write(f"Score: {self.score}  High Score: {self.high_score}", False, align="center", font=('Arial', 12, 'normal'))