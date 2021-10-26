from turtle import Screen

SCREEN_WIDTH = 1200
SCREEN_HEIGHT = 900

screen = Screen()
screen.setup(width=SCREEN_WIDTH, height=SCREEN_HEIGHT)
screen.bgcolor("black")
screen.title("Snake")
screen.tracer(0)