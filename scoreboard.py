from turtle import Turtle
from screen import screen, SCREEN_WIDTH, SCREEN_HEIGHT

ALIGNMENT = "center"
FONT = ("Arial", 24, "normal")

class Scoreboard(Turtle):

   def __init__(self):
      super().__init__()
      self.score = 0
      with open("data.txt") as file:
         self.high_score = int(file.read())
      self.color("white")
      self.penup()
      self.goto(0, SCREEN_HEIGHT/2 -50)
      self.hideturtle()
      self.refresh_score()


   def refresh_score(self):
      self.clear()
      self.write("Score: {} High Score: {}".format(self.score, self.high_score), align=ALIGNMENT, font=FONT)


   def reset(self):
      if self.score > self.high_score:
         self.high_score = self.score
         with open("data.txt", mode="w") as file:
            file.write(f"{self.high_score}")
      self.score = 0
      self.refresh_score()









