from turtle import*
import random
franklin= Turtle()

def drawtriangle():
	for x in range(3):
		franklin.forward(100)
		franklin.left(120)

for x in range(12):
	drawtriangle()
	franklin.left(30)

mainloop()