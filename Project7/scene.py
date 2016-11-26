# Tony Karalekas
# Spring 2015
# CS 151 Project 7
#
# scene.py version 1
#---------------------------------------------
# imports

import sys
import turtle
import lsystem as ls
import turtle_interpreter as it 

#----------------------------------------------
turtle.tracer(False)

# background code
def grass():
	turtle.begin_fill()
	turtle.color("Green")
	turtle.speed(100)
	turtle.forward(1000)
	turtle.right(90)
	turtle.forward(1000)
	turtle.right(90)
	turtle.forward(2000)
	turtle.right(90)
	turtle.forward(1000)
	turtle.right(90)
	turtle.forward(1000)
	turtle.end_fill()
	
def sky():
	turtle.begin_fill()
	turtle.color("Blue")
	turtle.speed(100)
	turtle.forward(1000)
	turtle.left(90)
	turtle.forward(1000)
	turtle.left(90)
	turtle.forward(2000)
	turtle.left(90)
	turtle.forward(1000)
	turtle.left(90)
	turtle.forward(1000)
	turtle.end_fill()
	
def house():
	turtle.begin_fill()
	turtle.color('Red')
	turtle.forward(50)
	turtle.right(90)
	turtle.forward(50)
	turtle.right(90)
	turtle.forward(100)
	turtle.right(90)
	turtle.forward(50)
	turtle.right(90)
	turtle.forward(50)
	turtle.end_fill()
	
	turtle.begin_fill()
	turtle.color("Beige")
	turtle.forward(75)
	turtle.left(120)
	turtle.forward(150)
	turtle.left(120)
	turtle.forward(150)
	turtle.left(120)
	turtle.forward(75)
	turtle.end_fill()


#--------------------------------------------------

# lsystems in scene

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
	turtle.pencolor('Brown')
	it.drawString( s1, dist, angle1 )
	
	# wait and update
	turtle.update()
	
def tree2(argv, x, y):
	lsys_filename2 = argv[2]
	lsys2 = ls.createLsystemFromFile( lsys_filename2 )
	print lsys2
	num_iter2 = int( 3 )
	dist = float( 5 )
	angle2 = float( 30 )
	
	s2 = ls.buildString( lsys2, num_iter2 )
	
	#draw lsystem2
	'''this is my second lsystem
		with filename mysystem2.txt
		with 5 iterations and
		with angle = 120 dist = 10'''
	turtle.up()
	turtle.goto(0,0)
	turtle.goto(x,y)
	turtle.down()
	turtle.setheading(0)
	turtle.left(90)
	turtle.pencolor('White')
	it.drawString( s2, dist, angle2 )
	
	# wait and update
	turtle.update()
	
def sun(argv):
	lsys_filename3 = argv[3]
	lsys3 = ls.createLsystemFromFile( lsys_filename3 )
	print lsys3
	num_iter3 = int( 3 )
	dist = 5
	angle3 = float( 120 )
	
	s3 = ls.buildString( lsys3, num_iter3 )
	
	#draw lsystem3
	'''this is my third lsystem
		with filename mysystem3.txt
		with 3 iterations and
		with angle = 45 dist = 10'''
	turtle.up()
	turtle.goto(0,0)
	turtle.goto(300, 200)
	turtle.down()
	turtle.setheading(0)
	turtle.left(90)
	turtle.pencolor('Red')
	it.drawString( s3, dist, angle3 )
	

	# wait and update
	turtle.update()
	
# main calling code
grass()
sky()
sun(sys.argv)
turtle.up()
turtle.goto(0,0)
turtle.setheading(0)
turtle.left(90)
turtle.down()
tree1(sys.argv, 0,0)
tree2( sys.argv, 50, 0)
tree1(sys.argv, 100,0)
tree2( sys.argv, 150, 0)
tree1(sys.argv, 200,0)
tree2( sys.argv, 250, 0)
tree1(sys.argv, 300,0)
tree2( sys.argv, -50, 0)
tree1(sys.argv, -100,0)
tree2( sys.argv, -150, 0)
tree1(sys.argv, -200,0)
tree2( sys.argv, -250, 0)
tree1(sys.argv, -300,0)
tree1(sys.argv, 0,-100)
tree2( sys.argv, 50,-100)
tree1(sys.argv, 100,-100)
tree2( sys.argv, 150, -100)
tree1(sys.argv, 200,-100)
tree2( sys.argv, 250, -100)
tree1(sys.argv, 300,-100)
tree2( sys.argv, -50, -100)
tree1(sys.argv, -100,-100)
tree1(sys.argv, 0,-200)
tree2( sys.argv, 50,-200)
tree1(sys.argv, 100,-200)
tree2( sys.argv, 150, -200)
tree1(sys.argv, 200,-200)
tree2( sys.argv, 250, -200)
tree1(sys.argv, 300,-200)
tree2( sys.argv, -50, -200)
tree1(sys.argv, -100,-200)
turtle.up()
turtle.goto(0,0)
turtle.goto(-300, -200)
turtle.setheading(0)
turtle.down()
house()

it.hold()

raw_input("Press enter to continue")