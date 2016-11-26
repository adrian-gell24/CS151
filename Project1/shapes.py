# imports
from turtle import *

# set up code 
tracer(False)

# shape definitions
def shapeA():
	forward(100)
	left(120)
	forward(100)
	left(120)
	forward(100)
	left(120)

def shapeB():
	forward(100)
	left(60)
	forward(100)
	left(60)
	forward(100)
	left(60)
	forward(100)
	left(60)
	forward(100)
	left(60)
	forward(100)
	left(60)
	
def shapeC():
	shapeA()
	forward(100)
	shapeB()
	
def shapeD( distance ):
	forward( distance )
	left(72)
	forward( distance )
	left(72)
	forward( distance )
	left(72)
	forward( distance )
	left(72)
	forward( distance )
	left(72)
	
def shapeE():
	shapeD(25)
	shapeD(50)
	shapeD(100)
	shapeD(150)
	shapeD(200)

# drawing code
shapeE()

# finishing code
update()
raw_input("Hit Enter to Continue")