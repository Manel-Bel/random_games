import turtle
import math 


wn = turtle.Screen()
wn.title('drawing by manel ')
wn.bgcolor('black')
wn.setup(width=1300, height=900)


line = turtle.Turtle()
line.color('white')
line.speed(5)
count = 0
while count < 4 :
   line.forward(200)
   line.left(90)
   count += 1
line.clear()

triangle = turtle.Turtle()
triangle.speed(5)
triangle.color('red')
triangle.goto(-200,0)
triangle.forward(200)
triangle.left(90)
triangle.forward(200)
triangle.left(135)
triangle.forward((200**2 +200**2)**0.5)
triangle.clear()

#star
star = turtle.Turtle()
star.speed(5)
star.color('white')
count = 0 
c = (100**2 + 100**2 -2*100*100*math.cos(math.pi/6))**0.5
while count < 5 :
    star.forward(300)
    star.left(144)
    count += 1 
star.clear()

count = 0
shape = turtle.Turtle()
shape.color('white')
shape.speed(5)
shape.left(90)
shape.forward(100)
count = 0
while count < 4:
    shape.right(90//2)
    if count != 3:
        shape.forward(50)
    else:
        shape.forward(100)
    count = count + 1
shape.right(90)
shape.forward(130)
#       ____
#      /    \
#      |     |
#      |_____|
shape.clear()

snail = turtle.Turtle()
snail.speed(0)
snail.color('white')
colors = ["blue", "green", "purple", "cyan", "magenta", "violet"]
for i in range(45):
    snail.color(colors[i % 6])
    snail.pendown()
    snail.fd(2 + i * 5)
    snail.left(45)
    snail.width(i)
    snail.penup()
snail.clear()

cool_shape = turtle.Turtle()
cool_shape.reset()
cool_shape.speed(20)
cool_shape.color('white')
b = 200 
while b > 0 :
    cool_shape.left(b)
    cool_shape.forward(b * 3)
    b -= 1

#cercle
count = 0
circle = turtle.Turtle()
circle.color('blue')
circle.speed(30)
while(count < 360):
    circle.forward(1)
    circle.left(1)
    count = count + 1