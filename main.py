from snake import Snake
from food import Food
from scoreboard import Scoreboard
from screen import screen, SCREEN_WIDTH, SCREEN_HEIGHT

import time


snake = Snake()
food = Food()
scoreboard = Scoreboard()

# CONTROL THE SNAKE WITH KEYBOARD
screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")


game_is_on = True
while game_is_on:
    screen.update()
    time.sleep(0.05)
    snake.move()

    # DETECT COLLISION WITH FOOD
    if snake.head.distance(food) < 20:
        snake.extend()
        food.refresh()
        scoreboard.score += 1
        scoreboard.refresh_score()

    # DETECT COLLISION WITH WALL
    if snake.head.xcor() > SCREEN_WIDTH/2  or snake.head.xcor() < -SCREEN_WIDTH/2  \
            or snake.head.ycor() > SCREEN_HEIGHT/2  or snake.head.ycor() < -SCREEN_HEIGHT/2 :
        scoreboard.reset()
        snake.reset()

    # DETECT COLLISION WITH TAIL
    for segment in snake.segments[1:]:
        if snake.head.distance(segment) < 10:
            scoreboard.reset()
            snake.reset()




screen.exitonclick()