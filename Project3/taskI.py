# Tony Karalekas
# Spring 2015
# CS 151 Project 3

#====================================================================

# import different modules 
import turtle as t
import random
import better_shapelib as bsl

#-------------------------------

# Task 5
# Position and Scale three separate myscene() images 
'''For Task 5 I have decided to use myscene2() which
	is the second Maine outdoors scene from my project2'''

if __name__ == '__main__':	
	bsl.myscene2(400,200,.10)
	bsl.goto(0, 0)
	t.setheading(0)
	bsl.myscene2(-450, 200, .15)
	bsl.goto(0, 0)
	t.setheading(0)
	bsl.myscene2( 0, -100, .25)
	bsl.goto(0, 0)
	t.setheading(0)

# used goto() and setheading() to bring turtle cursor back to start point	

t.update()


raw_input('Press enter to continue')