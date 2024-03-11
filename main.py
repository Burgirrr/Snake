import turtle
import time
import random

screen = turtle.Screen()
screen.tracer(0)
screen.setup(600,600)

head = turtle.Turtle()
head.shape("square")
head.penup()
head.direction = "Stop"

food = turtle.Turtle()
food.shape("circle")
food.penup()
food.goto(random.randint(-200,200), random.randint (-200, 200))

score = turtle.Turtle()
score.penup()
score.hideturtle()
score.goto(-100, 250)
s = 0
high_s = 0
score.write("Score: " + "High Score: " + str(high_s), move=False,
font=("Arial", 20, "bold"))

def up() :
    head.direction = "up"
def down () :
    head.direction = "down"
def left () :
    head.direction = "left"
def right () :
    head.direction = "right"

def move () :
    if head.direction == "up":
        head.sety(head.ycor() + 20)
    if head.direction == "down":
        head.sety(head.ycor() - 20)
    if head.direction == "right":
        head.setx(head.xcor() + 20)
    if head.direction == "left":
        head.setx(head.xcor() - 20)


screen.listen()
screen.onkeypress(up, "w")
screen.onkeypress(down, "s")
screen.onkeypress(left, "a")
screen.onkeypress(right, "d")




x = []
y = []
body = []
lose = False
while lose == False:
    x.append(head.xcor())
    y.append(head.ycor())


    move()

    if head.distance(food) < 20:
        food.goto(random.randint(-250,250), random.randint(-250,250))
        b = turtle.Turtle()
        b.penup()
        b.shape("square")
        b.color("gray")
        body.append(b)
        s += 10
        score.clear()
        score.write("Score: " + str(s) + "High Score: " + str(high_s), move=False, font=("Arial", 20, "bold"))

    for i in range(len(body)):
        body[i].goto(x[-1 - i], y[-1 - i])

        if body[i].distance (head) < 20:
            head.goto(0, 0)
            for b in body:
             b.hideturtle()
            body = []
            if s > high_s:
             high_s = s
            s = 0
            score.clear()
            score.write("Score: " + str(s) + "High Score: " + str(high_s), move=False, font=("Arial", 20, "bold"))
            screen.update()
            head.direction = "Stop"
            time.sleep(2)
            break

    screen.update()
    time.sleep(0.1)

screen.mainloop()