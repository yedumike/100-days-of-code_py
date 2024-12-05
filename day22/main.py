from turtle import Turtle, Screen
import random
danitello = Turtle()

directions = ["left","right","forward","back"]
colors = ["cyan","lawn green","spring green","gold","dark magenta","dark orchid","peru","tan","red","blue","yellow","orange red"]

distance = 20
def moves(direction):
    if direction == "left":
        danitello.left(90)
        danitello.forward(distance)
    if direction == "right":
        danitello.right(90)
        danitello.forward(distance)
    if direction == "back":
        danitello.back(distance)
    if direction == "forward":
        danitello.forward(distance)

screen = Screen()
screen.bgcolor("black")

def up():
    danitello.setheading(90)
    danitello.forward(20)
def down():
    danitello.setheading(270)
    danitello.forward(20)
def left():
    danitello.setheading(180)
    danitello.forward(20)
def right():
    danitello.setheading(0)
    danitello.forward(20)


danitello.width(6)
danitello.speed("fastest")
screen.listen()
screen.onkey(up,"Up")
screen.onkey(down,"Down")
screen.onkey(left,"Left")
screen.onkey(right,"Right")
for i in range(10000):
    danitello.color(random.choice(colors))
    direct = random.choice(directions)
    if 1 % 100 == 0:
        danitello.up(100)
    moves(direct)



screen.exitonclick()
