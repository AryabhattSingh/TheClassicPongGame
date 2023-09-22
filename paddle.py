from turtle import Turtle


class Paddle(Turtle):
    def __init__(self, x_pos, y_pos):
        super().__init__()
        self.shape("square")
        self.color("white")
        self.shapesize(stretch_wid=5, stretch_len=1)
        self.penup()
        self.goto(x_pos, y_pos)

    def upwards(self):
        new_x = self.xcor()
        new_y = self.ycor() + 20
        if new_y < 260:
            self.goto(new_x, new_y)

    def downwards(self):
        new_x = self.xcor()
        new_y = self.ycor() - 20
        if new_y > -260:
            self.goto(new_x, new_y)
