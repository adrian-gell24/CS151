# imports
from turtle import *

# set up code
tracer(False)

# definitions
def shape(distance , nsides):
	for i in range(0,nsides):
		forward(distance)
		left(360.0/nsides)

# drawing code
shape(100 , 3)
shape(100 , 4)
shape(100 , 5)
shape(100 , 6)
shape(100 , 7)
shape(100 , 8)
shape(100 , 9)
shape(100 , 10)
shape(100 , 11)

# help from vlad!

# finishing code
update()
raw_input("Hit Enter to Continue")