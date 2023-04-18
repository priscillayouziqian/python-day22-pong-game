from turtle import Turtle


class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.color("white")
        self.penup()
        self.x_move = 10
        self.y_move = 10
        self.move_speed = 0.1

    def move(self):
        new_x = self.xcor() + self.x_move
        new_y = self.ycor() + self.y_move
        self.goto(new_x, new_y)

    def bounce_y(self):
        self.y_move *= -1  # the -1 is to make the line 14 add calculation to become subtraction - moving the opposite direction

    def bounce_x(self):
        self.x_move *= -1  # reversing the x direction
        self.move_speed *= 0.9  # each time the ball bounces the paddle, it increases the speed. for speed(0.001) is faster than speed(0.1)

    def reset_position(self):
        self.goto(0, 0)
        self.move_speed = 0.1 # set speed back to default / original: 0.1
        self.bounce_x()