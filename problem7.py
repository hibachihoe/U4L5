from turtle import *

franklin = Turtle()

franklin.color("black")
franklin.pensize(3)
franklin.speed(5)
franklin.shape("turtle")

def drawstar():
	for x in range(5):
		franklin.forward(50)
		franklin.left(144)

def row():
	for y in range(3):
		drawstar()
		franklin.penup()
		franklin.forward(60)
		franklin.pendown()

for z in range(4):
	row()
	franklin.penup()
	franklin.backward(180)
	franklin.right(90)
	franklin.forward(60)
	franklin.left(90)
	franklin.pendown()

mainloop()