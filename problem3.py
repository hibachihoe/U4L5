from turtle import*
import random
franklin= Turtle()

def drawhexagon():
	for x in range(6):
		franklin.forward(100)
		franklin.left(60)

drawhexagon()

mainloop()