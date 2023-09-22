from turtle import Turtle


class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.color("white")
        self.goto(x=0, y=0)
        self.penup()

    def move(self):
        while self.xcor() < 280:
            new_x = self.xcor() + 25
            new_y = self.ycor() + 20

            self.goto(new_x, new_y)