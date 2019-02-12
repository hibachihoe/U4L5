from turtle import*
import random
franklin= Turtle()

def drawtriangle():
	for x in range(3):
		franklin.forward(100)
		franklin.left(120)

drawtriangle()

mainloop()