# Tony Karalekas
# Spring 2015
# CS 151 Project 8
#
# growth.py version 1
#---------------------------------------------
#
# Task 3, Project 8
#
#==========================================================================
#
# imports

import lsystem as ls
import turtle_interpreter as it
import turtle

#---------------------------------------------
turtle.tracer(False)

def grass():
	turtle.up()
	turtle.goto(-2000,2000)
	turtle.down()
	turtle.begin_fill()
	turtle.color("ForestGreen")
	turtle.forward(4000)
	turtle.right(90)
	turtle.forward(4000)
	turtle.right(90)
	turtle.forward(4000)
	turtle.right(90)
	turtle.forward(4000)
	turtle.right(90)
	turtle.forward(4000)
	turtle.end_fill()

def river():
	turtle.up()
	turtle.goto(-100,0)
	turtle.left(75)
	turtle.down()
	turtle.begin_fill()
	turtle.color("Blue")
	turtle.forward(1000)
	turtle.right(90)
	turtle.forward(250)
	turtle.right(90)
	turtle.forward(2000)
	turtle.right(90)
	turtle.forward(250)
	turtle.right(90)
	turtle.forward(1000)
	turtle.end_fill()
	
def sky():
	turtle.up()
	turtle.goto(0,350)
	turtle.setheading(0)
	turtle.down()
	turtle.begin_fill()
	turtle.color("SteelBlue")
	turtle.forward(1000)
	turtle.right(90)
	turtle.forward(200)
	turtle.right(90)
	turtle.forward(2000)
	turtle.right(90)
	turtle.forward(200)
	turtle.right(90)
	turtle.forward(1000)
	turtle.end_fill()

def sun():
	turtle.up()
	turtle.goto(50,200)
	turtle.begin_fill()
	turtle.color("Red")
	turtle.circle(75)
	turtle.end_fill()

def boat():
	turtle.up()
	turtle.goto(-75,-150)
	turtle.down()
	turtle.begin_fill()
	turtle.color('Brown')
	turtle.forward(150)
	turtle.left(90)
	turtle.forward(50)
	turtle.left(90)
	turtle.forward(150)
	turtle.left(90)
	turtle.forward(50)
	turtle.left(90)
	turtle.end_fill()
	turtle.up()
	turtle.goto(0,-100)
	turtle.down()
	turtle.begin_fill()
	turtle.color('White')
	turtle.forward(10)
	turtle.left(90)
	turtle.forward(75)
	turtle.left(90)
	turtle.forward(10)
	turtle.left(90)
	turtle.forward(75)
	turtle.left(90)
	turtle.end_fill()
	turtle.goto(-1,-40)
	turtle.down()
	turtle.begin_fill()
	turtle.color('Black')
	turtle.left(30)
	turtle.forward(50)
	turtle.left(120)
	turtle.forward(50)
	turtle.left(120)
	turtle.forward(50)
	turtle.end_fill()



# main function to draw collection of lsystem trees
def tree1(iters, xpos, ypos):
	'''Creates lsystem from filename and then creates an arrangement'''
	# creates object from lsystem
	l1 = ls.Lsystem('mylsystem1.txt')
	
	#number of iterations
	# for growth effect in task 3, made iters a parameter
	num_iter1 = iters
	
	#creates buildstring function
	s1 = l1.buildString(num_iter1)
	
	#specific angle
	angle = 15
	
	#creates an object from TI class
	ti = it.TurtleInterpreter()
	
	# sets the colors of the tracer and calls the drawstring function
	# orients the trees with parameters xpos and ypos
	# My Tree 1 (mylsystem1.txt)
	turtle.pencolor('DarkOliveGreen')
	turtle.pensize(2)
	'''tree with stem color of olivedrab'''
	turtle.up()
	turtle.setposition(xpos,ypos)
	turtle.setheading(90)
	turtle.down()
	ti.drawString(s1,10,angle)

def tree2(iters, xpos, ypos):
	'''Creates lsystem from filename and then creates an arrangement'''
	# creates object from lsystem
	l2 = ls.Lsystem('mylsystem2.txt')
	
	#number of iterations
	# for growth effect in task 3, made iters a parameter
	num_iter2 = iters
	
	# creates buildstring function
	s2 = l2.buildString(num_iter2)
	
	#specific angle
	angle2 = 30
	
	#creates an object from TI class
	ti = it.TurtleInterpreter()
	
	# sets the colors of the tracer and calls the drawstring function
	# orients the trees  with parameters xpos and ypos
	# My Tree 2 (mylsystem2.txt)
	turtle.pencolor('SandyBrown')
	'''tree with stem color of coral'''
	turtle.up()
	turtle.setposition(xpos,ypos)
	turtle.setheading(90)
	turtle.down()
	ti.drawString(s2,7,angle2)

	
def main():
	turtle.goto(0,0)
	tree1(2, -500, -300)
	turtle.up()
	turtle.goto(0,0)
	turtle.down()
	tree1(2, -300, -300)
	turtle.up()
	turtle.goto(0,0)
	turtle.down()
	tree1(3, -300, -200)
	turtle.up()
	turtle.goto(0,0)
	turtle.down()
	tree1(3, -500, -200)
	turtle.up()
	turtle.goto(0,0)
	turtle.down()
	tree1(4, -400, -50)
	turtle.up()
	turtle.goto(0,0)
	turtle.down()
	tree1(4, -150, -100)
	turtle.up()
	turtle.goto(0,0)
	turtle.down()
	tree2(2, 500, -300)
	turtle.up()
	turtle.goto(0,0)
	turtle.down()
	tree2(2, 300, -300)
	turtle.up()
	turtle.goto(0,0)
	turtle.down()
	tree2(3, 350, -250)
	turtle.up()
	turtle.goto(0,0)
	turtle.down()
	tree2(4, 500, -150)
	turtle.up()
	turtle.goto(0,0)
	turtle.down()
	tree2(4, 200, -200)
	

def scene():
	grass()
	river()
	sky()
	sun()
	boat()

if __name__ == "__main__":
	scene()
	main()
	
raw_input( "Press enter to continue" )