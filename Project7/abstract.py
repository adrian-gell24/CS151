# Tony Karalekas
# Spring 2015
# CS 151 Project 7
#
# abstract.py version 1
#---------------------------------------------
# imports

import sys
import turtle
import lsystem as ls
import turtle_interpreter as it 

#----------------------------------------------

# test code 
def main(argv):

	# check if there are enough arguments
	if len(argv) < 10:
		print "Usage : python abstract.py 3*<in_filename> 3*<num_iterations>"
		exit()
	
	# assign lsys_filenames to command line filename arguments
	lsys_filename1 = argv[1]
	lsys_filename2 = argv[2]
	lsys_filename3 = argv[3]

	# create the lsystems from a file
	lsys1 = ls.createLsystemFromFile( lsys_filename1 )
	lsys2 = ls.createLsystemFromFile( lsys_filename2 )
	lsys3 = ls.createLsystemFromFile( lsys_filename3 )
	print lsys1
	print lsys2
	print lsys3

	# assign num_interations to command line number arguments
	num_iter1 = int( argv[4] )
	num_iter2 = int( argv[5] )
	num_iter3 = int( argv[6] )
	
	# build the lsystem string with given number of iterations
	s1 = ls.buildString( lsys1, num_iter1 )
	s2 = ls.buildString( lsys2, num_iter2 )
	s3 = ls.buildString( lsys3, num_iter3 )
	print s1
	print s2
	print s3
	
	# assign distances and angles to given command line inputs 
	dist = float( argv[7] )
	angle1 = float( argv[8] )
	angle2 = float( argv[9] )
	angle3 = float( argv[10] )


	# draw the lsystems
	#draw lsystem1
	'''this is my first lsystem
		with filename mysystem1.txt
		with 3 iterations and
		with angle = 45 dist = 10'''
	turtle.tracer(False)
	turtle.up()
	turtle.goto(-400, 0)
	turtle.down()
	turtle.left(90)
	turtle.pencolor('Green')
	it.drawString( s1, dist, angle1 )
	
	#draw lsystem2
	'''this is my second lsystem
		with filename mysystem2.txt
		with 5 iterations and
		with angle = 120 dist = 10'''
	turtle.up()
	turtle.goto(0,0)
	turtle.goto(0,0)
	turtle.down()
	turtle.setheading(0)
	turtle.left(90)
	turtle.pencolor('Red')
	it.drawString( s2, dist, angle2 )
	
	#draw lsystem3
	'''this is my third lsystem
		with filename mysystem3.txt
		with 3 iterations and
		with angle = 45 dist = 10'''
	turtle.up()
	turtle.goto(0,0)
	turtle.goto(300,-100)
	turtle.down()
	turtle.setheading(0)
	turtle.left(90)
	turtle.pencolor('Blue')
	it.drawString( s3, dist, angle3 )
	

	# wait and update
	turtle.update()
	it.hold()
	
# main calling code
if __name__ == '__main__':
	main(sys.argv)