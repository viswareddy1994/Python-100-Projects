from turtle import Turtle
ALIGNMENT = "center"
FONT = ('Courier', 16, 'bold')
class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.color("White")
        self.goto(0,270)
        self.hideturtle()
        self.score = 0
        self.high_score = self.updated_high_score()
        self.update_scoreboard()
    
    def update_scoreboard(self):
        self.clear()
        self.write(arg= f"Your Score: {self.score} High Score: {self.high_score}", move=False ,align=ALIGNMENT,font=FONT)
    
    def high_score_update(self,val):
        with open(r"C:\Python\turtle_graphics\snake_game\data\data.txt", mode="w") as file:
            file.write(val)
    def updated_high_score(self):
        with open(r"C:\Python\turtle_graphics\snake_game\data\data.txt", mode="r") as file:
            val = file.read()
            return int(val)
        

    def reset(self):
        if self.score > self.high_score:
            self.high_score_update(val=str(self.score))
            self.high_score = self.updated_high_score()
        self.score = 0
        self.update_scoreboard()
    # def game_over(self):
    #     self.goto(0,0)
    #     self.write("GAME OVER", align=ALIGNMENT,font=FONT)
    
    def calculate_score(self):
        self.score +=1
        self.update_scoreboard()
        
        


    

        
            