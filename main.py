from turtle import Screen
from paddle import Paddle
from ball import Ball
import time


screen = Screen()
screen.setup(width=800, height=600)
screen.bgcolor("black")
screen.title("My Pong Game")
screen.tracer(0)  # turn off the animation, needs manually update the screen later

r_paddle = Paddle((350, 0))
l_paddle = Paddle((-350, 0))
ball = Ball()

screen.listen()
screen.onkey(r_paddle.go_up, "Up")
screen.onkey(r_paddle.go_down, "Down")
screen.onkey(l_paddle.go_up, "w")  # can't create two event listeners share one key "Up", here use w to distinguish
screen.onkey(l_paddle.go_down, "s")  # same above


game_is_on = True

while game_is_on:
    time.sleep(0.1)  # have the ball to move every refresh of the screen
    screen.update()
    ball.move()

screen.exitonclick()