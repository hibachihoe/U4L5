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

drawstar()

franklin.penup()
franklin.forward(100)
franklin.pendown()
drawstar()

franklin.penup()
franklin.backward(200)
franklin.pendown()
drawstar()
mainloop()
