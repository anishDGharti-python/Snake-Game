from turtle import Turtle


ALIGNMENT = 'center'
FONTS = ("Verdana", 15, "normal")
class ScoreBoard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        with open('../../../Desktop/data.txt') as data:
            self.high_score = int(data.read())
        self.penup()
        self.color("white")
        self.hideturtle()
        self.goto(0, 270)

        self.update_scoreboard()

    def update_scoreboard(self):
        self.clear()
        self.write(align=ALIGNMENT, move=False, font=FONTS, arg=f"Score: {self.score}  High Score: {self.high_score}")

    def increase_score(self):
        self.score += 20  
        self.update_scoreboard()

    def reset(self):
        if self.score > self.high_score:
            self.high_score = self.score
            with open('../../../Desktop/data.txt', mode='w') as score:
                score.write(f'{self.high_score}')        
        self.score = 0    
        self.update_scoreboard()





    # def game_over(self):
    #     self.penup()
    #     self.goto(0,0)
        
    #     self.write(align=ALIGNMENT,move=False, font=FONTS, arg="Game Over" )    