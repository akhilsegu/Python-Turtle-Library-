import turtle
t=turtle.Turtle()
w=turtle.Screen()
w.title("Olympic Rings")
t.speed(10)
t.pensize(6)

#Black Ring
t.pencolor("black")
t.circle(80)

#Blue Ring
t.penup()
t.goto(-200, 0)
t.pendown()
t.pencolor("blue")
t.circle(80)

#Red Ring
t.penup()
t.goto(200, 0)
t.pendown()
t.pencolor("red")
t.circle(80)

# Yellow Ring
t.penup()
t.goto(-100, -100)
t.pendown()
t.pencolor("yellow")
t.circle(80)

#Green Ring
t.penup()
t.goto(100, -100)
t.pendown()
t.pencolor("green")
t.circle(80)

t.ht()

