# -*- coding: utf-8 -*-
"""
Created on Tue Apr 19 22:16:00 2022

@author: shykul
"""
#Method-01

# import library
import turtle
import math

# setup Turtle
wn = turtle.Screen()
wn.setup(1000,800)
myTurtle = turtle.Turtle()  # set turtle to x = 0 and y = 0 on screen
myTurtle.pensize(3)


def main():             # this function calculate the value of fib and sends the results to the draw function
    valueOne = 0
    valueTwo = 1
    fib = 1
    for i in range(8):                      # number of squares to draw
        myTurtle.right(90)                  # point turtle to down position
        drawSq(fib*20)                      # call drawSq function-  argument = length of sides
        fib = valueOne + valueTwo           # calculate the value of Fibonacci
        valueOne = valueTwo
        valueTwo = fib
        
# this function draws the Fibonacci square
def drawSq(sides):
    for n in range(6):                     # the value 6 ensures that the start of the next square is correct
        myTurtle.forward(sides)            # draw the sides of the squares
        myTurtle.left(90)                  # turn pointer left 90 degrees


def sprial():
    r = 20                                 # draws to size of the radius
    angle = 90
    myTurtle.right(90)                     # turn turtle to down position
    myTurtle.penup()
    myTurtle.setpos(0,0)                   # move turtle to starting point of first square
    myTurtle.pendown()
    # draw fibonacci spiral
    arc(20, angle)                         # call arc function  1 * 20 = 20
    arc(20, angle)                         # call arc function  1 * 20 = 20
    arc(40, angle)                         # call arc function  2 * 20 = 40
    arc(60, angle)                         # call arc function  3 * 20 = 60
    arc(100, angle)                        # call arc function  5 * 20 = 100
    arc(160,angle)                         # call arc function 8 * 20 = 160
    arc(260,angle)                         # call arc function 13 * 20 = 260
    arc(420,angle)                         # call arc function 21 * 20 = 420


def arcLine(n, length, angle):            # Draws n line segments.
    for i in range(n):
        myTurtle.forward(length)
        myTurtle.left(angle)


def arc(r, angle):                        #  Draws an arc with the given radius and angle
    arc_length = 2 * math.pi * r * abs(angle) / 360
    n = int(arc_length / 4) + 1
    step_length = arc_length / n
    step_angle = float(angle) / n
    # Before starting making a slight left turn.
    myTurtle.left(step_angle/2)
    arcLine(n, step_length, step_angle)
    myTurtle.right(step_angle/2)


# main program loop
main()                                     # calls the main function which draws the boxes
sprial()                                   # calls the spiral function which draws the sprial
wn.exitonclick()                           # click on the screen to exit the program

#Method-02
import turtle as tur
import time


class Fibonacci:
    def __init__(self, max_width):
        self.list = [0, 1]
        while self.list[len(self.list)-1] < max_width:
            self.i = self.list[len(self.list)-1] + self.list[len(self.list)-2]
            self.list.append(self.i)

    def main(self, x, y, square_colour, arc_colour):
        self.square(square_colour, x, y)
        self.arc(arc_colour, x, y)

    def square(self, colour, x, y):
        tur.pu()
        tur.goto(x, y)
        tur.seth(270)
        tur.color(colour)
        tur.pd()
        tur.width(3)
        tur.speed(5)
        for i in self.list:
            for j in range(5):
                tur.forward(i)
                tur.right(90)
            tur.forward(i)

    def arc(self, colour, x, y):
        tur.pu()
        tur.goto(x, y)
        tur.seth(90)
        tur.color(colour)
        tur.pd()
        tur.width(2)
        tur.speed(1)
        for i in self.list:
            tur.circle(-i, 90)


x = -232
y = -143
while True:
    tur.bgcolor("white")
    tur.ht()
    fibonacci = Fibonacci(500).main(x, y, "black", "black")
    time.sleep(10)
    tur.reset()
tur.done()