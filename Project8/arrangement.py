# Tony Karalekas
# Spring 2015
# CS 151 Project 8
#
# arrangement.py version 1
#---------------------------------------------
#
# Task 2, Project 8
#
#==========================================================================
#
# imports

import lsystem as ls
import turtle_interpreter as it
import turtle

#---------------------------------------------
turtle.tracer(False)

# main function to draw collection of lsystem trees
def main():
	'''Creates 5 lsystems from filenames and then creates an arrangement'''
	# creates object from lsystem
	l1 = ls.Lsystem('systemCL.txt')
	l2 = ls.Lsystem('systemDL.txt')
	l3 = ls.Lsystem('systemEL.txt')
	l4 = ls.Lsystem('systemFL.txt')
	l5 = ls.Lsystem('systemGL.txt')
	
	# different iteration number for separate trees
	num_iter1 = 2
	num_iter2 = 3
	num_iter3 = 3
	num_iter4 = 3
	num_iter5 = 5
	
	# creates buildstring functions with specific num_iters
	s1 = l1.buildString(num_iter1)
	s2 = l2.buildString(num_iter2)
	s3 = l3.buildString(num_iter3)
	s4 = l4.buildString(num_iter4)
	s5 = l5.buildString(num_iter5)
	
	# different angles for each tree and drawstring function
	angle = 30
	angle2 = 20
	angle3 = 15
	angle4 = 35
	angle5 = 25
	
	#creates an object from TI class
	ti = it.TurtleInterpreter()
	
	# sets the colors of the tracer and calls the drawstring function
	#orients the trees
	
	# Tree 1 (systemCL.txt)
	turtle.pencolor('OliveDrab')
	'''tree with stem color of olivedrab'''
	turtle.up()
	turtle.setposition(-500,-200)
	turtle.setheading(90)
	turtle.down()
	ti.drawString(s1,25,angle)
	
	# Tree 2 (systemDL.txt)
	turtle.pencolor('Coral')
	'''tree with stem color of coral'''
	turtle.up()
	turtle.setposition(-300,-200)
	turtle.setheading(90)
	turtle.down()
	ti.drawString(s2,25,angle2)
	
	# Tree 3 (systemEL.txt)
	'''tree with stem color of springgreen'''
	turtle.pencolor('SpringGreen')
	turtle.up()
	turtle.setposition(0,-200)
	turtle.setheading(90)
	turtle.down()
	ti.drawString(s3,25,angle3)
	
	# Tree 4 (systemFL.txt)
	'''tree with stem color of seagreen'''
	turtle.pencolor('SeaGreen')
	turtle.up()
	turtle.setposition(300,-200)
	turtle.setheading(90)
	turtle.down()
	ti.drawString(s4,25,angle4)
	
	# Tree 5 (systemGL.txt)
	'''tree with stem color of limegreen'''
	turtle.pencolor('LimeGreen')
	turtle.up()
	turtle.setposition(500,-200)
	turtle.setheading(90)
	turtle.down()
	ti.drawString(s5,10,angle5)
	
	ti.hold()
	

if __name__ == "__main__":
  main()