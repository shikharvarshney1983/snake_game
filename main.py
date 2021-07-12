import turtle as t
import time
from snake import Snake
from food import Food
from score import Score
    
screen = t.Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.tracer(0)

snake = Snake()
food = Food()
score = Score()

screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")

is_game_on = True

while is_game_on:
    screen.update()
    time.sleep(0.1)
    snake.move()

    if snake.segments[0].distance(food) < 15:
        food.refresh()
        score.increase_score()
        snake.extend()

    if snake.segments[0].xcor() > 280 or snake.segments[0].xcor() < -280 or snake.segments[0].ycor() > 280 or snake.segments[0].ycor() < -280:
        is_game_on = False
        score.game_over()

    for seg in snake.segments[1:]:
        if snake.segments[0].distance(seg) < 10:
            is_game_on = False
            score.game_over()

screen.exitonclick()        