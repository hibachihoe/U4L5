from turtle import *

franklin = Turtle()

franklin.color("red")
franklin.pensize(3)
franklin.speed(5)
franklin.shape("turtle")

def drawstar():
	for x in range(5):
		franklin.forward(50)
		franklin.left(144)

drawstar()

mainloop()
