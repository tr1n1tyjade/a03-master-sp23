######################################################################
# Author: David Brothers             TODO: Change this to your name, if modifying
# Username: brothersd                      TODO: Change this to your username, if modifying#
# Assignment: A02: Loopy Turtles
# Purpose: To demonstrate the turtle library and loops
######################################################################
# Acknowledgements:
#
# original from http://interactivepython.org/runestone/static/thinkcspy/index.html
# first modified by Dr. Jan Pearce
#
# licensed under a Creative Commons
# Attribution-Noncommercial-Share Alike 3.0 United States License.
#Google doc linkhttps://docs.google.com/document/d/1hQpibEoP1PHOIVsonx8yFGzPDqkq2h-yM4mXgyRGuUw/edit#
######################################################################

import turtle
import random

wn= turtle.Screen()
turtle= turtle.Turtle()
wn.colormode(255)
wn.bgcolor(1, 59, 200)
turtle.pencolor()


def bun():
    turtle.begin_fill()
    for i in range(2):
        turtle.forward(80)
        turtle.right(90)
        turtle.forward(30)
        turtle.right(90)
    turtle.fillcolor(100,90,100)
    turtle.end_fill()

def meat():
    turtle.begin_fill()
    turtle.fillcolor(200,100,100)
    turtle.left(120)
    turtle.forward(20)
    turtle.right(70)
    turtle.forward(30)
    turtle.right(50)
    turtle.forward(80)
    turtle.right(70)
    turtle.forward(30)
    turtle.right(70)
    turtle.forward(20)
    turtle.end_fill()
    turtle.right(70)
    turtle.forward(85)
    turtle.right(150)
def onions():
    turtle.begin_fill()
    for i in range(2):
        turtle.forward(80)
        turtle.left(90)
        turtle.forward(15)
        turtle.left(90)

    turtle.fillcolor(255, 90, 100)
    turtle.end_fill()
def main():
    bun()
    meat()
    onions()

main()
wn.exitonclick()

