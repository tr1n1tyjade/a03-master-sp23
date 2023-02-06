import turtle

def draw_square(t, x, y, size):
    t.penup()
    t.goto(x, y)
    t.pendown()
    for i in range(4):
        t.forward(size)
        t.left(90)

def draw_board(t, x, y, size, rows, columns):
    for row in range(rows):
        for col in range(columns):
            if (row + col) % 2 == 0:
                t.fillcolor("white")
            else:
                t.fillcolor("black")
            t.begin_fill()
            draw_square(t, x + col * size, y - row * size, size)
            t.end_fill()

def main():
    t = turtle.Turtle()
    t.speed(0)
    t.hideturtle()
    draw_board(t, -200, 200, 50, 8, 8)
    turtle.done()

if __name__ == '__main__':
    main()
