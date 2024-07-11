import math
import turtle


#turtle shape and colour configuration
turtle.bgcolor("black")
turtle.shape("turtle")
turtle.speed(0)


#we draw sunflower petals
turtle.goto(0, -40)
turtle.pendown()
h = 0
phi = 137.508 * (math.pi / 180.0)
for i in range(16):
    for j in range(18):
        turtle.color("yellow")
        h += 0.005
        turtle.rt(90)
        turtle.circle(150 - j * 6, 90)
        turtle.lt(90)
        turtle.circle(150 - j * 6, 90)
        turtle.rt(180)
    turtle.circle(40, 24)



#we draww the center of the sunflower
turtle.penup()
turtle.goto(0, 0)
turtle.color("black")
turtle.fillcolor("brown")
turtle.begin_fill()
turtle.circle(0)
turtle.end_fill()
phi = 137.508 * (math.pi / 180.0)
for i in range(160 + 40):
    r = 4 * math.sqrt(i)
    theta = i * phi
    x = r * math.cos(theta)
    y = r * math.sin(theta)
    turtle.penup()
    turtle.goto(x, y)
    turtle.setheading(i * 137.508)
    turtle.pendown()
    if i < 160:
        turtle.stamp()



#we write the text
turtle.penup()
turtle.goto(0, 300)
turtle.color("White")
turtle.write("Para el campus de profundización científica 2024", align="center", font=("Arial", 24, "bold"))

#wait till user closes
turtle.done()
