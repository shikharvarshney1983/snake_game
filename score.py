from turtle import Turtle

FONT = ("Arial", 10, "bold")

class Score(Turtle):

    def __init__(self):
        super().__init__()
        self.score = 0
        self.color("white")
        self.penup()
        self.goto(0,280)
        self.hideturtle()
        self.write(f"Score: {self.score}", False, align="center", font=FONT)

    def increase_score(self):
        self.score += 1
        self.undo()
        self.write(f"Score: {self.score}", False, align="center", font=FONT)

    def game_over(self):
        self.goto(0,0)
        self.write("GAME OVER", align="center", font=FONT)