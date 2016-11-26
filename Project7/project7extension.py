# Tony Karalekas
# Spring 2015
# CS 151 Project 7
#
# extension
#---------------------------------------------
# imports

import sys
import turtle
import lsystem as ls
import turtle_interpreter as it 
import better_shapelib as bsl
import random

#-----------------------------

def myscene2( x, y, scale ):
	'''scale and position dependent function of outdoors2 in project2'''
	bsl.landscape(x+0*scale, y+0*scale, 1*scale)
	bsl.lighthouse(x+0*scale, y+0*scale, 1*scale)
	bsl.wildlife(x+0*scale, y+0*scale, 1*scale)
	
def tree1(argv, x, y):
	lsys_filename1 = argv[1]
	lsys1 = ls.createLsystemFromFile( lsys_filename1 )
	print lsys1
	num_iter1 = int( 3 )
	dist = float( 5 )
	angle1 = float( 22 )
	
	s1 = ls.buildString( lsys1, num_iter1 )
	
	#draw lsystem1
	'''this is my first lsystem
		with filename mysystem1.txt
		with 3 iterations and
		with angle = 45 dist = 10'''
	turtle.tracer(False)
	turtle.speed(50000000)
	turtle.up()
	turtle.goto(0,0)
	turtle.goto(x, y)
	turtle.down()
	turtle.pencolor('White')
	it.drawString( s1, dist, angle1 )
	
	# wait and update
	turtle.update()
	
	
myscene2(0,0,1)
for i in range(50):
	turtle.up()
	turtle.goto(0,0)
	turtle.setheading(0)
	turtle.left(90)
	turtle.down
	tree1(sys.argv, random.randint(-400,400), random.randint(-400, 50))


raw_input("Press enter to continue")