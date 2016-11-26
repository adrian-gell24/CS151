# Tony Karalekas
# Spring 2015
# CS 151 Project 9
#
# turtle_interpreter.py version 3
#---------------------------------------------
#
# The purpose of this file is to convert a string
# into an image using simple turtle commands 
#
#==========================================================================
import turtle
import sys


class TurtleInterpreter:
	initialized = False

	def __init__(self, dx = 800, dy = 800):
		if TurtleInterpreter.initialized:
			return
		TurtleInterpreter.initialized = True
		turtle.setup()
		turtle.tracer(False)
		
	def drawString(self, dstring, distance, angle):
		stack = []
		cstack = []
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
			elif c == 'L':
				#draws a leaf
				#begin and end fil calls work better in this section of code
				turtle.begin_fill()
				turtle.circle(5)
				turtle.end_fill()
			elif c == 'Q':
				#created for task3
				#draws a flower
				turtle.begin_fill()
				turtle.right(90)
				turtle.forward(5)
				turtle.left(120)
				turtle.forward(10)
				turtle.left(120)
				turtle.forward(10)
				turtle.left(120)
				turtle.forward(10)
				turtle.end_fill()
			elif c == 'P':
				#draws a petal
				#CREATED FOR EXTENSION1
				turtle.begin_fill()
				for i in range(12):
					turtle.forward(5)
					turtle.right(108)
					turtle.forward(5)
					turtle.left(144)
				turtle.end_fill()
			elif c == '<':
				color = turtle.color()[0]
				cstack.append(color)
			elif c == '>':
				turtle.color(cstack.pop())
			elif c == 'g':
				#makes the leaf color medium orchid
				turtle.color("Medium Orchid")
			elif c == 'y':
				#makes the leaf color turquoise
				turtle.color("Turquoise")
			elif c == 'r':
				#makes the leaf color salmon
				turtle.color("Salmon")
			elif c == 'b':
				#CREATED FOR EXTENSION1
				#makes the leaf color salmon
				turtle.color("Plum")
			elif c == 'o':
				#CREATED FOR EXTENSION1
				#makes the leaf color salmon
				turtle.color("Khaki")
			elif c == '{':
				turtle.fill(True)
			elif c == '}':
				turtle.fill(False)
			
			
		turtle.update()
	
	def color(self, c):
		turtle.color = c
		
	def hold(self):
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
		
		
	def place(self, xpos, ypos, angle=None): 
		turtle.up()
		turtle.goto( xpos, ypos )
		if angle != None:
			turtle.setheading(angle)
		turtle.down()

	def orient(self, angle): 
		turtle.setheading(angle)

	def goto(self, xpos, ypos): 
		turtle.up()
		turtle.goto( xpos, ypos )
		turtle.down()
		
	def color(self, c): 
		turtle.color(c)
	
	def width(self, w): 
		turtle.width(w)

	
	
