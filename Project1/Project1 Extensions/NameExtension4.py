# imports
from turtle import *

# set up code 

# definitions
def T():
	forward(25)
	left(90)
	forward(200)
	right(90)
	forward(75)
	left(90)
	forward(25)
	left(90)
	forward(175)
	left(90)
	forward(25)
	left(90)
	forward(75)
	right(90)
	forward(200)
	
def O():
	circle(50)
	
def N():
	left(90)
	forward(100)
	right(150)
	forward(115)
	left(150)
	forward(100)
	
def Y():
	left(90)
	forward(75)
	right(30)
	forward(50)
	right(180)
	up()
	forward(50)
	right(120)
	down()
	forward(50)
	
	
def Tony():
	T()
	left(90)
	up()
	forward(75)
	down()
	O()
	up()
	forward(50)
	down()
	N()
	up()
	right(180)
	forward(100)
	left(90)
	forward(25)
	down()
	Y()
	
# drawing code
Tony()


# finishing code
update()
raw_input("Hit Enter to Continue")
