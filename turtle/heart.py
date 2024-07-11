import math
import turtle

def heart(k):
    return 15*math.sin(k)**3

def heart1(k):
    return 12*math.cos(k)-5*\
        math.cos(2*k)-2*\
        math.cos(3*k)-\
        math.cos(4*k)

turtle.speed(1000)
turtle.bgcolor('black')
for i in range(6000):
    turtle.goto(heart(i)*20,heart1(i)*20)
    for j in range(5):
        turtle.color('pink')

turtle.done()