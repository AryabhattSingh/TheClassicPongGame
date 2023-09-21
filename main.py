# Create a screen
from turtle import Screen, Turtle

screen = Screen()
screen.title("The Classic Pong Game")
screen.bgcolor("black")
screen.setup(width=800, height=600)

# Create and move a paddle
right_paddle = Turtle()
right_paddle.shape("square")
right_paddle.color("white")
right_paddle.shapesize(stretch_wid=5, stretch_len=1)
right_paddle.penup()
right_paddle.goto(350, 0)





def upwards():
    new_x = right_paddle.xcor()
    new_y = right_paddle.ycor() + 20
    if new_y < 260:
        right_paddle.goto(new_x, new_y)

def downwards():
    new_x = right_paddle.xcor()
    new_y = right_paddle.ycor() - 20
    if new_y > -260:
        right_paddle.goto(new_x, new_y)


screen.listen()
screen.onkeypress(upwards, "Up")
screen.onkeypress(downwards, "Down")



screen.exitonclick()
