from turtle import Turtle
MOVE_DISTANCE = 20
START_POSITION = [(0, 0), (-20, 0), (-40, 0)]
class Snake:

    def __init__(self):
        self.segment = []
        self.create_body()
        self.head = self.segment[0]
    def create_body(self):
        for body_part in START_POSITION:
            self.new_body(body_part)

    def new_body(self, position):
        snake = Turtle(shape="square")
        snake.color("yellow")
        snake.penup()
        self.segment.append(snake)
        snake.goto(position)
    def add_body(self):
        position = self.segment[-1].position()
        self.new_body(position)

    def move(self):
        for i in range(len(self.segment) - 1, 0, -1):
            new_position = i - 1
            x = self.segment[new_position].xcor()
            y = self.segment[new_position].ycor()
            self.segment[i].goto(x, y)
        self.head.forward(MOVE_DISTANCE)


    def reset_snake(self):
        for seg in self.segment:
            seg.goto(1000, 1000)
        self.segment.clear()
        self.create_body()
        self.head = self.segment[0]

    def turn_right(self):
        if self.head.ycor() != self.segment[1].ycor():
            self.head.setheading(0)

    def move_up(self):
        if self.segment[0].xcor() != self.segment[1].xcor():
            self.segment[0].setheading(90)

    def move_down(self):
        if self.segment[0].xcor() != self.segment[1].xcor():
            self.segment[0].setheading(270)

    def turn_left(self):
        if self.segment[0].ycor() != self.segment[1].ycor():
            self.segment[0].setheading(180)

