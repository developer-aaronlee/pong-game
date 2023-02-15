from turtle import Turtle
ALIGNMENT = "center"
FONT = ("Courier", 80, "normal")


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.color("white")
        self.penup()
        self.hideturtle()
        self.l_score = 0
        self.r_score = 0
        self.update_scoreboard()

    def update_scoreboard(self):
        self.clear()
        self.goto(0, 200)
        self.write(f"{self.l_score} vs {self.r_score}", align=ALIGNMENT, font=FONT)

    def l_add_score(self):
        self.l_score += 1
        self.update_scoreboard()

    def r_add_score(self):
        self.r_score += 1
        self.update_scoreboard()
