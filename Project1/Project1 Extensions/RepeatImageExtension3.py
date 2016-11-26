# imports
from turtle import *

# set up code

# shape definitions
def diamond(start , distance):
	left(start)
	forward(distance)
	left(60)
	forward(distance)
	left(120)
	forward(distance)
	left(60)
	forward(distance)
	
def trapezoid(start1 , distance1 , distance2):
	left(start1)
	forward(distance1)
	left(120)
	forward(distance2)
	left(60)
	forward(distance2)
	left(60)
	forward(distance2)
	

def star():
	diamond(45 , 50)
	diamond(60 , 50)
	diamond(60 , 50)
	diamond(60 , 50)
	diamond(60 , 50)
	diamond(60 , 50)
	diamond(45 , 100)
	diamond(60 , 100)
	diamond(60 , 100)
	diamond(60 , 100)
	diamond(60 , 100)
	diamond(60 , 100)
	trapezoid(45 , 100 , 50)
	trapezoid(60 , 100 , 50)
	trapezoid(60 , 100 , 50)
	trapezoid(60 , 100 , 50)
	trapezoid(60 , 100 , 50)
	trapezoid(60 , 100 , 50)
	trapezoid(45 , 200 , 100)
	trapezoid(60 , 200 , 100)
	trapezoid(60 , 200 , 100)
	trapezoid(60 , 200 , 100)
	trapezoid(60 , 200 , 100)
	trapezoid(60 , 200 , 100)

# drawing code
star()

# finishing code
update()
raw_input("Hit Enter to Continue")
