from turtle import Turtle
from screen import screen, SCREEN_WIDTH, SCREEN_HEIGHT

import random

class Food(Turtle):

   def __init__(self):
      super().__init__()
      self.shape("circle")
      self.penup()
      self.color("midnight blue")
      self.speed("fastest")
      self.refresh()


   def refresh(self):
      x = random.randint(-SCREEN_WIDTH/2 + 40, SCREEN_WIDTH/2 -40)
      y = random.randint(-SCREEN_HEIGHT/2 + 40, SCREEN_HEIGHT/2 -40)
      self.goto(x, y)








