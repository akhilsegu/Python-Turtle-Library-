import turtle
t=turtle.Turtle()
w=turtle.Screen()
w.title("India Flag")
t.speed(10)


#Go to start position
t.up()
t.goto(-400,260)
t.down()

t.color("orange")
t.begin_fill()
t.forward(800)
t.right(90)
t.forward(167)
t.right(90)
t.forward(800)
t.end_fill()

t.color("white")
t.begin_fill()
t.lt(90)
t.forward(167)

t.color("green")
t.begin_fill()
t.forward(167)
t.lt(90)
t.forward(800)
t.lt(90)
t.forward(167)
t.end_fill()

# Blue Circle
t.up()
t.goto(70, 0)
t.down()
t.color("navy")
t.begin_fill()
t.circle(70)
t.end_fill()

# White Circle next
t.up()
t.goto(60, 0)
t.down()
t.color("white")
t.begin_fill()
t.circle(60)
t.end_fill()

# Mini Blue Circles
t.up()
t.goto(-57, -8)
t.down()
t.color("navy")

# Small Blue Circle
t.up()
t.goto(20, 0)
t.down()
t.begin_fill()
t.circle(20)
t.end_fill()

# Spokes
t.up()
t.goto(0, 0)
t.down()
t.pensize(2)
for i in range(24):
    t.forward(60)
    t.backward(60)
    t.left(-15)

t.ht()

