from turtle import Turtle
FONT = ('Courier', 20, 'bold')
ALIGNMENT = "center"

class ScoreBoard(Turtle):

    def __init__(self):
        super().__init__()
        self.score = 0
        with open("data.txt") as data:
            self.high_score = int(data.read())
        self.color("white")
        self.hideturtle()
        self.goto(0, 265)
        self.score_count()

    def score_count(self):
        self.clear()
        self.write(arg=f"Pontos: {self.score} Highscore: {self.high_score}", align=ALIGNMENT, font=FONT)

    def reset_score(self):
        if self.score > self.high_score:
            self.high_score = self.score
            with open("data.txt", mode="w") as data:
                data.write(f"{self.high_score}")
        self.score = 0
        self.score_count()

    def increase_score(self):
        self.score += 1
        self.score_count()

    # def game_over(self):
    #     self.goto(0, 0)
    #     self.write(arg="FIM DO JOGO", align=ALIGNMENT, font=FONT)
