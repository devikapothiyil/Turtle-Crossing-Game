from turtle import Turtle

FONT = ("Courier", 24, "normal")

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.level=1
        self.hideturtle()
        self.penup()
        self.score()

    def game_over(self):
        self.goto(0,0)
        self.write("GAME OVER", align="center", font=FONT)

    def score(self):
        self.clear()
        self.goto(-280, 250)
        self.write(f"Level:{self.level}", align="left", font=FONT)

    def increase_level(self):
        self.level+=1
        self.score()
