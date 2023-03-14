from turtle import Turtle, Screen

ALIGNMENT = "center"
FONT = ("Courier", 24, "normal")


class ScoreBoard(Turtle):

    def __init__(self):
        super().__init__()
        self.score = 0
        with open("data.txt") as file:
            self.high_score= int(file.read())



        self.color("white")
        self.penup()
        self.goto(0, 270)
        self.update_scoreboard()
        self.hideturtle()

    def update_scoreboard(self):
        self.clear()
        self.write(f"Score: {self.score} Highest score:{self.high_score}", align=ALIGNMENT, font=FONT)

    def reset(self):
        if self.score > self.high_score:
            self.high_score = self.score
            with open("data.txt",mode='w') as data:
                data.write(f"{self.high_score}")


        self.score = 0
        self.update_scoreboard()




    def game_over(self):
        self.goto(0,0)
        self.write(f"game over ", align=ALIGNMENT, font=FONT)

    def increase_score(self):

        self.score +=1

        self.update_scoreboard()