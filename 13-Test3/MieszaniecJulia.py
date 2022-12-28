import turtle
tur=turtle.Turtle()
tur.speed(1)



def triangle():
    tur.color('black','green')
    tur.begin_fill()
    for x in range(3):
        tur.forward(200)
        tur.left(120)
    tur.end_fill()

def right():
    tur.color('black','red')
    tur.begin_fill()
    tur.forward(25)
    tur.left(135)
    tur.forward(35)
    tur.left(135)
    tur.forward(25)
    tur.end_fill()

def cross():
    tur.color('black','yellow')
    tur.begin_fill()
    for x in range(4):
        tur.forward(15)
        tur.right(90)
        tur.forward(15)
        tur.left(90)
        tur.forward(15)
        tur.left(90)
    tur.end_fill()

def parallelogram():
    tur.color('black','pink')
    tur.begin_fill()
    for x in range(2):
        tur.forward(35)
        tur.left(50)
        tur.forward(20)
        tur.left(130)
    tur.end_fill()

def rhombus():
    tur.color('blue','orange')
    tur.begin_fill()
    for x in range(2):
        tur.left(60)
        tur.forward(40)
    tur.left(120)
    tur.forward(40)
    tur.left(60)
    tur.forward(40)
    tur.end_fill()

#choinka   
for i in range(4):
    triangle()
    tur.penup()
    tur.right(90)
    tur.forward(100)
    tur.left(90)
    tur.pendown()


tur.penup()
tur.left(90)
tur.forward(150)
tur.right(90)
tur.pendown()
for x in range(5):
    rhombus()
    tur.penup()
    tur.left(60)
    tur.forward(50)
    tur.pendown()


tur.penup()
tur.left(90)
tur.forward(150)
tur.left(90)
tur.forward(50)
tur.pendown()
for x in range(4):
    right()
    tur.penup()
    tur.left(90)
    tur.forward(50)
    tur.pendown()


tur.penup()
tur.right(90)
tur.forward(150)
tur.right(90)
tur.pendown()
for x in range(4):
    parallelogram()
    tur.penup()
    tur.forward(50)
    tur.pendown()

tur.penup()
tur.left(90)
tur.forward(120)
tur.left(90)
tur.forward(100)
tur.right(90)
tur.pendown()
for x in range(8):
    tur.right(45)
    cross()


def name():
    tur.penup(); tur.setpos(0,250); tur.pendown(); tur.color("black")
    tur.write("Julia Mieszaniec ZZISS1-1113", move=True, align="left", font=("Arial", 20))

name()

ts = turtle.getscreen()

ts.getcanvas().postscript(file="JuliaMieszaniec.jpg")