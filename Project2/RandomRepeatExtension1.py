# Tony Karalekas
# Spring 2015
# CS 151 Project 2 Extension1 

#====================================================================
 
import turtle
 
import random
 
import shapelib
 
 
def extension1():
	turtle.tracer(False)
	for i in range(50):
		turtle.setheading( random.randint(0,360))
		shapelib.parallelogram( random.randint(-350,-250),
							random.randint(-300, 300),
							random.random(), 'red')
	for i in range(50):
		turtle.setheading( random.randint(0,360))
		shapelib.cross( random.randint(-200, -100),
						random.randint(-300, 300),
						random.random(), 'yellow')
	for i in range(50):
		turtle.setheading( random.randint(0,360))
		shapelib.star( random.randint(-50, 50),
						random.randint(-300, 300),
						random.random(), 'pink')
	for i in range(50):
		turtle.setheading( random.randint(0,360))
		shapelib.star( random.randint(100, 200),
							random.randint(-300, 300),
							random.random(), 'orange')
	for i in range(50):
		turtle.setheading( random.randint(0,360))
		shapelib.cross( random.randint(250, 350),
						random.randint(-300, 300),
						random.random(), 'green')
	for i in range(50):
		turtle.setheading( random.randint(0,360))
		shapelib.parallelogram( random.randint(400, 500),
						random.randint(-300, 300),
						random.random(), 'blue')
						
						
turtle.update()
					
extension1()

raw_input('Press enter to continue')