import time
from turtle import Screen, Turtle
from snake import Snake
from food import Food
from scoreboard import ScoreBoard

screen = Screen()
screen.setup(width=600, height=600)
screen.title("Jogo da Cobrinha")
screen.bgcolor("green")
screen.tracer(0)

snake = Snake()
screen.listen()
apple = Food()
score = ScoreBoard()

screen.onkey(fun=snake.turn_left, key="a")
screen.onkey(fun=snake.turn_right, key="d")
screen.onkey(fun=snake.move_up, key="w")
screen.onkey(fun=snake.move_down, key="s")

game_is_on = True
while game_is_on:
    screen.update()
    time.sleep(0.1)
    snake.move()
    if snake.head.distance(apple) < 15:
        apple.refresh()
        score.increase_score()
        snake.add_body()

    if snake.head.xcor() > 290 or snake.head.xcor() < -290 or snake.head.ycor() > 290 or snake.head.ycor() < -290:
        snake.reset_snake()
        score.reset_score()

    for body_part in snake.segment[1:]:
        if snake.segment[0].position() == body_part.position():
            snake.reset_snake()
            score.reset_score()


screen.exitonclick()

