import random
from turtle import Turtle, Screen

leonardo = Turtle()
screen = Screen()

# leonardo.shape("turtle")
# n = 3
# angle = 360/n
colors = ["cyan","lawn green","spring green","gold","dark magenta","dark orchid","peru","tan","red","blue","yellow","orange red"]
def draw_shape(sides):
    angle = 360/sides
    for _ in range(sides) :
        leonardo.forward(90)
        leonardo.left(angle)


for sides in range(3,11):
    leonardo.color(random.choice(colors))
    draw_shape(sides)
# angles = [120,90,72,60,360/7]
# sides = 3
# for angle in angles:

#     sides += 1




# leonardo.forward(10)
# leonardo.penup()
# leonardo.forward(10)
# leonardo.pendown()
# leonardo.forward(10)
# leonardo.penup()
# leonardo.forward(10)
# leonardo.pendown()
# leonardo.forward(10)



# leonardo.forward(100)
# leonardo.up()
# leonardo.right(90)
# print(leonardo.isdown())
# leonardo.down()
# leonardo.forward(100)
# leonardo.up()
# print(leonardo.isdown())

# leonardo.right(90)
# leonardo.down()
# print(leonardo.isdown())

# leonardo.forward(100)
# leonardo.up()
# leonardo.right(90)

screen.exitonclick()
