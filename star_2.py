import turtle 
from random import randint as rint

win = turtle.Screen()
win.setup(900, 500)
spiral = turtle.Turtle()
spiral.speed(10)
win.bgcolor('black')
couleur1 = ['yellow', 'green']
couleur2 = ['blue', 'red', 'purple']
couleurst = ['blue', 'yellow', 'white','green']
c =0 
for i in range(50) :
    spiral.forward(i * 10 )
    spiral.right(144)
    spiral.color(couleurst[rint(0, len(couleurst)-1)])