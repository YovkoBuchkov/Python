import turtle


def draw_pumpkin():
    screen = turtle.Screen()
    screen.bgcolor("black")
    pumpkin = turtle.Turtle()
    pumpkin.color("orange")
    pumpkin.pensize(3)
    pumpkin.speed(10)

    def tri(x, y, color):
        pumpkin.penup()
        pumpkin.goto(x, y)
        pumpkin.begin_fill()
        pumpkin.color(color)
        pumpkin.pendown()
        for _ in range(3):
            pumpkin.forward(20)
            pumpkin.right(120)
        pumpkin.end_fill()

    def eyes(x, y, z, color):
        pumpkin.penup()
        pumpkin.goto(x, y)
        pumpkin.begin_fill()
        pumpkin.color(color)
        pumpkin.pendown()

        for _ in range(3):
            pumpkin.forward(z)
            pumpkin.right(120)

        pumpkin.end_fill()

    # Draw the pumpkin
    pumpkin.penup()
    pumpkin.goto(10, -60)
    pumpkin.pendown()
    pumpkin.begin_fill()
    pumpkin.circle(100)
    pumpkin.end_fill()

    pumpkin.penup()
    pumpkin.goto(-40, -60)
    pumpkin.pendown()
    pumpkin.begin_fill()
    pumpkin.circle(100)
    pumpkin.end_fill()

    # Draw the stem
    eyes(-40, 160, 50, 'green')

    # Draw the mouth
    tri(-55, 10, '#fff')
    tri(-35, 10, '#fff')
    tri(-15, 10, '#fff')
    tri(5, 10, '#fff')
    tri(25, 10, '#fff')


    # Draw the eyes
    eyes(20, 100, 50, '#fff')

    eyes(-80, 100, 50, '#fff')

    pumpkin.left(180)

    # Draw the nose
    eyes(10, 30, 40, '#000')

    # Draw the teeth
    tri(-35, -30, '#fff')
    tri(-15, -30, '#fff')
    tri(5, -30, '#fff')
    tri(25, -30, '#fff')
    tri(40, -30, '#fff')

    eyes(-10, -55, 10, '#663300')

    #blood
    pumpkin.penup()
    pumpkin.goto(-30, -10)
    pumpkin.pendown()
    pumpkin.color("red")
    pumpkin.begin_fill()
    pumpkin.setheading(-60)
    pumpkin.circle(30, 120)
    pumpkin.setheading(240)
    pumpkin.circle(30, 120)
    pumpkin.end_fill()


    # Hide turtle
    pumpkin.hideturtle()
    screen.mainloop()

draw_pumpkin()
