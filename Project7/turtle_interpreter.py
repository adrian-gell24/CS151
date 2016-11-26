# Tony Karalekas
# Spring 2015
# CS 151 Project 7
#
# turtle_interpreter.py version 1
#---------------------------------------------
#
# The purpose of this file is to convert a string
# into an image using simple turtle commands 
#
#==========================================================================
# imports
import turtle
import sys

#-------------------------------

def drawString( dstring, distance, angle ):
    """ Interpret the characters in string dstring as a series
    of turtle commands. Distance specifies the distance
    to travel for each forward command. Angle specifies the
    angle (in degrees) for each right or left command. The list of 
    turtle supported turtle commands is:
    F : forward
    - : turn right
    + : turn left
    [ : save position, heading
    ] : restore position, heading
    """
    stack = []
    for c in dstring:
		if c == 'F':
			turtle.forward(distance)
		elif c == '-':
			turtle.right(angle)
		elif c == '+':
			turtle.left(angle)
		elif c == '[':
			stack.append(turtle.position())
			stack.append(turtle.heading())
		elif c == ']':
			turtle.up()
			turtle.setheading(stack.pop())
			turtle.goto(stack.pop())
			turtle.down()
		turtle.update()
	

def hold():
    """ holds the screen open until the user clicks or types 'q' """

    # have the turtle listen for events
    turtle.listen()

    # hide the turtle and update the screen
    turtle.ht()
    turtle.update()

    # have the turtle listen for 'q'
    turtle.onkey( turtle.bye, 'q' )
    # have the turtle listen for a click
    turtle.onscreenclick( lambda x,y: turtle.bye() )

    # start the main loop until an event happens, then exit
    turtle.mainloop()
    exit()

