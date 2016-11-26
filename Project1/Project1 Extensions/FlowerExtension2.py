# imports
from turtle import *

# set up code


# definitions
def stem(distance):
	left(90)
	forward(distance)
	
def leaves():
	left(90)
	forward(50)
	right(40)
	forward(25)
	right(120)
	forward(25)
	right(120)
	forward(25)
	right(80)
	forward(50)
	left(40)
	forward(25)
	left(120)
	forward(25)
	left(120)
	forward(25)
	left(80)
	forward(100)
	
def petals(distance):
	forward(distance)
	right(144)
	forward(distance)
	right(144)
	forward(distance)
	right(144)
	forward(distance)
	right(144)
	forward(distance)
	right(144)

def flower():
	stem(200)
	right(180)
	forward(200)
	left(90)
	leaves()
	left(20)
	petals(100)


# drawing code
flower()

# finishing code
update()
raw_input("Hit Enter to Continue")