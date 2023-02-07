############################################################
# Name: Zaki Ayoubi
# Username: Ayoubim
# Google Doc Link: https://docs.google.com/document/d/1jfH5x7QutJ6QJgSUxd8SjumJCcupkgFu8Ujy9zlvfpw/edit#
############################################################

import turtle

def drawsquare (zaki, l, w):
    for i in range(2):
        zaki.forward(l)
        zaki.left(90)
        zaki.forward(w)
        zaki.left(90)

def main ():
    wn = turtle.Screen()
    wn.bgcolor("light green")
    zaki = turtle.Turtle()
    zaki.penup()
    zaki.setpos(-120, -100)
    zaki.pendown()
    drawsquare(zaki, 300, 200)
    zaki.penup()
    zaki.setpos(-90, 0)
    zaki.pendown()
    drawsquare(zaki, 60, 60)
    zaki.penup()
    zaki.setpos(100, 0)
    zaki.pendown()
    drawsquare(zaki, 60, 60)
    zaki.penup()
    zaki.setpos(100, 0)
    zaki.pendown()
    wn.exitonclick()

main()



