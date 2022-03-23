from turtle import Turtle
import random

class Ball(Turtle):
    
    random_list=[-1,1]

    def __init__(self) -> None:
        super().__init__()
        self.shape("circle")
        self.penup()
        self.color("white")
        self.goto(0, 0)
        random_list=[-1,1]
        self.x_move = 10*random.choice(random_list)
        self.y_move = 10*random.choice(random_list)
        self.move_speed = 0.1

    def move(self):
        x_cor = self.xcor() + self.x_move
        y_cor = self.ycor() + self.y_move
        self.goto(x_cor, y_cor)

    def bounce_y(self):
        self.y_move*=-1

    def bounce_x(self):
        self.x_move*=-1
        self.move_speed*=0.9

    def reset_position(self):
        self.goto(0,0)
        self.move_speed = 0.1
        self.bounce_x()
