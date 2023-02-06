import turtle

def mountain():
    t = turtle.Turtle()
    t.speed(4)
    t.penup()
    t.goto(-90, -300)
    t.pendown()
    for i in range(4):
        t.forward(400)
        t.left(90)
        t.fd(10)
def trail():
    t1 = turtle.Turtle()
    t1.speed(1)
    t1.penup()
    t1.goto(-300, 180)
    t1.pendown()
    t1.pensize(30)
    t1.pencolor("#D2BC91")
    for i in range(5):
        t1.right(40)
        t1.forward(60)
        t1.left(30)
        t1.forward(60)
def trees():
    t2 = turtle.Turtle()
    t2.speed(10)
    t2.penup()
    t2.goto(-300, 250)
    t2.pendown()
    for i in range(3):
        t2.left(80)
        t2.fd(60)
        t2.right(120)
        t2.fd(60)
        t2.right(120)
        t2.fd(63)
        t2.bk(31)
       # t2.left(70)
       # t2.fd(50)
        #t2.left(30)
        #t2.fd(40)









def main():
    win = turtle.Screen()
    turtle.Screen().bgcolor("#BFEDFB")
    mountain()
    trail()
    trees()
    win.exitonclick()

main()