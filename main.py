from turtle import Screen
from ball import Ball
from paddle import Paddle
from scoreboard import Scoreboard
import time

screen = Screen()
screen.bgcolor("black")
screen.setup(height=600, width=800)
screen.title("PONG")
screen.tracer(0)

right_paddle = Paddle((350, 0))
left_paddle = Paddle((-350, 0))
ball = Ball()
score = Scoreboard()
screen.update()

screen.listen()
screen.onkey(right_paddle.go_up, "Up")
screen.onkey(right_paddle.go_down, "Down")
screen.onkey(left_paddle.go_up, "w")
screen.onkey(left_paddle.go_down, "s")

game_is_on = True
while game_is_on:
    time.sleep(ball.move_speed)
    screen.update()
    ball.move()

    # Detect collision with Upper and Lower wall
    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce_y()

    # Detect collision with right paddle
    if ball.xcor() > 320 and ball.distance(right_paddle) < 50 or ball.xcor() < -320 and ball.distance(left_paddle) < 50:
        ball.bounce_x()

    if ball.xcor() > 380:
        ball.reset_position()
        score.left_point()

    if ball.xcor() < -380:
        ball.reset_position()
        score.right_point()

screen.exitonclick()