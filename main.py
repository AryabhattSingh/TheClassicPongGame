# Create a screen
import time
from turtle import Screen, Turtle

from ball import Ball
from paddle import Paddle
from scoreboard import Scoreboard

screen = Screen()
screen.title("The Classic Pong Game")
screen.bgcolor("black")
screen.setup(width=800, height=600)
# turn off the animation
screen.tracer(0)

# Create paddles
right_paddle = Paddle(x_pos=350, y_pos=0)
left_paddle = Paddle(x_pos=-350, y_pos=0)
# Create ball
ball = Ball()
# Create score
score = Scoreboard()

screen.listen()
screen.onkeypress(right_paddle.upwards, "Up")
screen.onkeypress(right_paddle.downwards, "Down")
screen.onkeypress(left_paddle.upwards, "w")
screen.onkeypress(left_paddle.downwards, "s")

game_on = True
while game_on:
    time.sleep(ball.move_speed)
    ball.move()

    # detect collision with wall
    if ball.ycor() > 270 or ball.ycor() < -270:
        ball.wall_bounce()

    # detect collision with paddle
    if (ball.distance(right_paddle) < 50 and ball.xcor() > 320) or (ball.distance(left_paddle) < 50 and ball.xcor() < -320):
        ball.paddle_bounce()

    # detect when right paddle misses
    if ball.xcor() > 400:
        ball.reset_position()
        score.left_score += 1
        score.update_score()

    # detect when left paddle misses
    if ball.xcor() < -400:
        ball.reset_position()
        score.right_score += 1
        score.update_score()

    screen.update()

screen.exitonclick()
