# Tony Karalekas
# Spring 2015
# CS 151 Project 8
#
# EXTENSION 1
#---------------------------------------------
#
# Extension 1, Project 8
#
#==========================================================================
#
# imports

import lsystem as ls
import turtle_interpreter as it
import turtle

#---------------------------------------------
turtle.tracer(False)

def main():
	'''Creates lsystem from filename and then creates an arrangement'''
	# creates object from lsystem
	l = ls.Lsystem('lsystemextension2.txt')
	
	#number of iterations
	# for growth effect in task 3, made iters a parameter
	num_iter = 4
	
	
	# creates buildstring function
	s = l.buildString(num_iter)
	
	#specific angle
	angle = 30
	
	#creates an object from TI class
	ti = it.TurtleInterpreter()
	
	# sets the colors of the tracer and calls the drawstring function
	turtle.pencolor('ForestGreen')
	'''tree with stem color of forestgreen'''
	turtle.up()
	turtle.setposition(0,0)
	turtle.setheading(90)
	turtle.down()
	ti.drawString(s, 50 ,angle)
	
	
	
	ti.hold()
	
	
if __name__ == "__main__":
	main()