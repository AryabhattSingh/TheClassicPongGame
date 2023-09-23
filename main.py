# Create a screen
import time
from turtle import Screen, Turtle

from ball import Ball
from paddle import Paddle

screen = Screen()
screen.title("The Classic Pong Game")
screen.bgcolor("black")
screen.setup(width=800, height=600)
# turn off the animation
screen.tracer(0)

# Create right paddle
right_paddle = Paddle(x_pos=350, y_pos=0)
left_paddle = Paddle(x_pos=-350, y_pos=0)
# Create ball
ball = Ball()
screen.tracer(1)

screen.listen()
screen.onkey(right_paddle.upwards, "Up")
screen.onkeypress(right_paddle.downwards, "Down")
screen.onkeypress(left_paddle.upwards, "w")
screen.onkeypress(left_paddle.downwards, "s")

game_on = True
while game_on:
    time.sleep(0.05)
    ball.move()

    # detect collision with wall
    #print(ball.xcor())
    #print (ball.ycor())

    if ball.ycor() > 270 or ball.ycor() < -270:
        ball.wall_bounce()

    # detect collision with paddle
    print(ball.distance(right_paddle))
    if ball.distance(right_paddle) < 30 or ball.distance(left_paddle) < 30:
        ball.paddle_bounce()

    screen.update()


screen.exitonclick()
