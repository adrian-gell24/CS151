# Tony Karalekas
# Spring 2015
# CS 151 Project 2

#====================================================================

# coding notes from lab2 on 2/12/15


# import different modules 
import turtle
import random

# all of the following functions are from lab work
def goto( x, y ):
	'''sends the turtle to location (x,y) without drawing'''
	print 'Sending turtle to' , x,y
	turtle.up()
	turtle.goto( x, y )
	turtle.down()

def block( x, y, width, height ):
	goto( x, y )
	
	print 'block(): drawing block of size', width, height
	# tell the turtle to go foward by width
	# tell the turtle to turn left by 90 degrees
	# tell the turtle to go forward by height
	# tell the turtle to turn left by 90 degrees
	# repeat the above 4 commands
	
	for i in range(2):
		turtle.forward(width)
		turtle.left(90)
		turtle.forward(height)
		turtle.left(90)	
		
def bunchOfBlocks( x, y, scale ):
    print 'bunchOfBlocks(): drawing blocks at location', x, y
    
    # put several calls to the block function here
    block( x, y, 45*scale, 90*scale )
    block( x+15*scale, y+90*scale, 15*scale, 30*scale )
    block( x+20*scale, y+120*scale, 5*scale, 15*scale )

def table( x, y, scale ):
	'''draws a table given the location and scale'''
	block( x-170*scale, y+100*scale, 200*scale, 20*scale)
	block( x-20*scale, y+0*scale, 20*scale, 100*scale)
	block( x-140*scale, y+0*scale, 20*scale, 100*scale)

# in my code for project2 i do not use table(), bunchOfBlocks(), or block()
# i rewrite the block() function as buildingblocks()
# i do use the function goto()
	
	
	
		
#====================================================================
	
	
# All of the following functions were created by me(Tony) for Lab 2

# Task 2 
# Simple Shape Functions
# parallelogram , star , and cross
 

def parallelogram( x, y, scale, color ):
	'''draws a parallelogram given location, scale, and color'''
	goto( x, y )
	turtle.begin_fill()
	turtle.color(color)
	turtle.forward(100*scale)
	turtle.left(60)
	turtle.forward(50*scale)
	turtle.left(120)
	turtle.forward(100*scale)
	turtle.left(60)
	turtle.forward(50*scale)
	turtle.end_fill()

def star( x, y, scale, color ):
	'''draws a star given location, scale, and color'''
	goto( x, y )
	turtle.begin_fill()
	turtle.color(color)
	turtle.forward(50*scale)
	turtle.right(108)
	turtle.forward(50*scale)
	turtle.left(144)
	turtle.forward(50*scale)
	turtle.right(108)
	turtle.forward(50*scale)
	turtle.left(144)
	turtle.forward(50*scale)
	turtle.right(108)
	turtle.forward(50*scale)
	turtle.left(144)
	turtle.forward(50*scale)
	turtle.right(108)
	turtle.forward(50*scale)
	turtle.left(144)
	turtle.forward(50*scale)
	turtle.right(108)
	turtle.forward(50*scale)
	turtle.left(144)
	turtle.forward(50*scale)
	turtle.right(108)
	turtle.forward(50*scale)
	turtle.left(144)
	turtle.forward(50*scale)
	turtle.right(108)
	turtle.forward(50*scale)
	turtle.left(144)
	turtle.forward(50*scale)
	turtle.right(108)
	turtle.forward(50*scale)
	turtle.left(144)
	turtle.forward(50*scale)
	turtle.right(108)
	turtle.forward(50*scale)
	turtle.left(144)
	turtle.forward(50*scale)
	turtle.right(108)
	turtle.forward(50*scale)
	turtle.left(144)
	turtle.end_fill()
	
def cross( x, y, scale, color ):
	'''draws a cross given location, scale, and color'''
	goto( x, y )
	turtle.begin_fill()
	turtle.color(color)
	turtle.forward(50*scale)
	turtle.right(90)
	turtle.forward(50*scale)
	turtle.left(90)
	turtle.forward(15*scale)
	turtle.left(90)
	turtle.forward(50*scale)
	turtle.right(90)
	turtle.forward(50*scale)
	turtle.left(90)
	turtle.forward(15*scale)
	turtle.left(90)
	turtle.forward(50*scale)
	turtle.right(90)
	turtle.forward(50*scale)
	turtle.left(90)
	turtle.forward(15*scale)
	turtle.left(90)
	turtle.forward(50*scale)
	turtle.right(90)
	turtle.forward(50*scale)
	turtle.left(90)
	turtle.forward(15*scale)
	turtle.end_fill()
	
	
	
	
#====================================================================

# Task 3 
# Outdoor Shapes Functions
# leaf and tree

def leaf( x, y, scale, color ):
	'''draws a leaf given location and scale'''
	goto( x, y )
	turtle.begin_fill()
	turtle.color(color)
	turtle.right(30)
	turtle.forward(8.33*scale)
	turtle.left(120)
	turtle.forward(3.33*scale)
	turtle.right(105)
	turtle.forward(15*scale)
	turtle.left(110)
	turtle.forward(5*scale)
	turtle.right(95)
	turtle.forward(15*scale)
	turtle.left(150)
	turtle.forward(15*scale)
	turtle.right(95)
	turtle.forward(5*scale)
	turtle.left(110)
	turtle.forward(15*scale)
	turtle.right(105)
	turtle.forward(3.33*scale)
	turtle.left(120)
	turtle.forward(8.33*scale)
	turtle.left(60)
	turtle.forward(10*scale)
	turtle.left(30)
	turtle.forward(10*scale)
	turtle.left(180)
	turtle.forward(10*scale)
	turtle.left(75)
	turtle.end_fill()
	turtle.forward(8.33*scale)
	
def tree( x, y, scale ):
	'''draws a leaf given location and scale'''
	goto( x, y )
	turtle.setheading(0)
	turtle.begin_fill()
	turtle.color('dark green')
	turtle.forward(25*scale)
	turtle.left(150)
	turtle.forward(25*scale)
	turtle.right(150)
	turtle.forward(20*scale)
	turtle.left(150)
	turtle.forward(30*scale)
	turtle.left(60)
	turtle.forward(30*scale)
	turtle.left(150)
	turtle.forward(20*scale)
	turtle.right(150)
	turtle.forward(25*scale)
	turtle.left(150)
	turtle.end_fill()
	turtle.forward(30*scale)
	goto( x, y )
	turtle.begin_fill()
	turtle.color('brown')
	turtle.right(90)
	turtle.forward(15*scale)
	turtle.right(90)
	turtle.forward(5*scale)
	turtle.right(90)
	turtle.forward(15*scale)
	turtle.right(90)
	turtle.end_fill()
	turtle.forward(5*scale)
	



#====================================================================

# Task 4 
# Functions for Outdoor1
# Mayflower Hill and Miller Library 
	
	
### functions for background() for Outdoor1

def cloud( x, y, scale, color):
	'''draws a cloud given location and scale'''
	goto( x, y )
	turtle.begin_fill()
	turtle.color(color)
	turtle.circle(50*scale)
	turtle.end_fill()
	turtle.begin_fill()
	turtle.color(color)
	turtle.up()
	turtle.forward(25*scale)
	turtle.down()
	turtle.circle(50*scale)
	turtle.end_fill()
	turtle.begin_fill()
	turtle.color(color)
	turtle.up()
	turtle.forward(35*scale)
	turtle.down()
	turtle.circle(50*scale)
	turtle.end_fill()
	turtle.begin_fill()
	turtle.color(color)
	turtle.up()
	turtle.forward(25*scale)
	turtle.down()
	turtle.circle(50*scale)
	turtle.end_fill()
	turtle.begin_fill()
	turtle.color(color)
	turtle.up()
	turtle.forward(25*scale)
	turtle.down()
	turtle.end_fill()

def sky( x, y, scale ):
	'''draws a huge blue square given location and scale'''
	turtle.tracer(False)
	turtle.begin_fill()
	turtle.color('light blue')
	buildingblock(x-1000, y+0, 2000*scale, 1075*scale)
	turtle.end_fill()

def grass( x, y, scale ):
	'''draws a huge blue square given location and scale'''
	turtle.tracer(False)
	turtle.begin_fill()
	turtle.color('green')
	buildingblock(x-1000, y-1000, 2000*scale, 1075*scale)
	turtle.end_fill()
	
def skyobjects( x, y, scale ):
	'''puts all of the objects in sky functions togehter'''
	turtle.tracer(False)
	star(x-300, y+225, 1*scale, 'orange')
	cloud(x+250, y+200, 1*scale, 'gray')
	cloud(x+175, y+125, 0.5*scale, 'gray')
	cloud(x+125, y+215, 0.25*scale, 'gray')

def background():
	sky(0,0,1)
	grass(0,0,1)
	skyobjects(0,0,1)
	
#--------------------------------

### functions for MillerLibrary()
	
def letterC( x, y, scale ):
	'''draws a letter C given location and scale'''
	goto(0,0)
	turtle.tracer(False)
	turtle.begin_fill()
	turtle.color('blue')
	buildingblock(x+25*scale, y+200, 50*scale, 10*scale)
	turtle.end_fill()
	turtle.begin_fill()
	turtle.color('blue')
	buildingblock(x-25*scale, y+225, 10*scale, 60*scale)
	turtle.end_fill()
	turtle.begin_fill()
	turtle.color('blue')
	buildingblock(x+25*scale, y+225, 50*scale, 10*scale)
	turtle.end_fill()
		
def buildingblock( x, y, width, height ):
# same code in block() function from lab 2
	'''building blocks for structures given location and scale'''
	goto( x, y )
	for i in range(2):
		turtle.forward(width)
		turtle.left(90)
		turtle.forward(height)
		turtle.left(90)
	
def MillerLibrary( x, y, scale ):
	''' Miller Library using buildingblocks()'''
	turtle.tracer(False)
	turtle.color('black')
	turtle.begin_fill()
	turtle.color('black')
	buildingblock(x-150, y+0, 300*scale, 100*scale)
	turtle.end_fill()
	turtle.begin_fill()
	turtle.color('gray')
	buildingblock(x-250, y+0, 100*scale, 50*scale)
	turtle.end_fill()
	turtle.begin_fill()
	turtle.color('gray')
	buildingblock(x+150, y+0, 100*scale, 50*scale)
	turtle.end_fill()
	turtle.begin_fill()
	turtle.color('white')
	buildingblock(x-125, y-25, 250*scale, 25*scale)
	turtle.end_fill()
	turtle.begin_fill()
	turtle.color('gray')
	buildingblock(x-100, y-50, 200*scale, 25*scale)
	turtle.begin_fill()
	turtle.color('white')
	buildingblock(x-75, y-75, 150*scale, 25*scale)
	turtle.end_fill()
	turtle.begin_fill()
	turtle.color('gray')
	buildingblock(x-50, y-100, 100*scale, 25*scale)
	turtle.end_fill()
	turtle.begin_fill()
	turtle.color('gray')
	buildingblock(x-100, y+100, 200*scale, 50*scale)
	turtle.end_fill()
	turtle.begin_fill()
	turtle.color('white')
	buildingblock(x-25, y+150, 50*scale, 100*scale)
	turtle.end_fill()
	turtle.begin_fill()
	turtle.color('gray')
	buildingblock(x-5, y+250, 10*scale, 40*scale)
	turtle.end_fill()
	turtle.begin_fill()
	turtle.color('blue')
	buildingblock(x-5, y+290, 10*scale, 10*scale)
	turtle.end_fill()
	turtle.begin_fill()
	turtle.color('blue')
	buildingblock(x-100, y+0, 15*scale, 100*scale)
	turtle.end_fill()
	turtle.begin_fill()
	turtle.color('blue')
	buildingblock(x-50, y+0, 15*scale, 100*scale)
	turtle.end_fill()
	turtle.begin_fill()
	turtle.color('blue')
	buildingblock(x-7.5, y+0, 15*scale, 100*scale)
	turtle.end_fill()
	turtle.begin_fill()
	turtle.color('blue')
	buildingblock(x+85, y+0, 15*scale, 100*scale)
	turtle.end_fill()
	turtle.begin_fill()
	turtle.color('blue')
	buildingblock(x+35, y+0, 15*scale, 100*scale)
	turtle.end_fill()
	# add decorations to the library
	# blue crosses and blue C
	cross(x-80, y+125, 0.25*scale, 'blue')
	cross(x+0, y+140, 0.25*scale, 'blue')
	cross(x+80, y+125, 0.25*scale, 'blue')
	turtle.up()
	turtle.left(90)
	turtle.down()
	letterC(0,0,0.5)
	
#--------------------------------	

### functions for MayflowerHill()

def flagpole( x, y, scale ):
	'''draws a flagpole given location and scale'''
	turtle.setheading(0)
	turtle.begin_fill()
	turtle.color('gray')
	buildingblock(x-25, y-350, 50*scale, 50*scale)
	turtle.end_fill()
	turtle.begin_fill()
	turtle.color('gray')
	buildingblock(x-15, y-300, 30*scale, 25*scale)
	turtle.end_fill()
	turtle.begin_fill()
	turtle.color('white')
	buildingblock(x-5, y-275, 10*scale, 100*scale)
	turtle.end_fill()
	turtle.begin_fill()
	turtle.color('blue')
	buildingblock(x-5, y-175, 50*scale, 25*scale)
	turtle.end_fill()

def foliageLeft():
	''' foliage scenery left side of image
			use tree() and leaf() functions defined earlier
			to make a variety of size and color foliage
			using for loops to make multiple'''
	turtle.tracer(False)
	for i in range(5):
		tree( random.randint( -300, -100 ),
				random.randint( -300, -100 ),
				random.randint( 1, 2 ))
	for i in range(10):
		leaf( random.randint( -300, -100 ),
				random.randint( -300, -100 ),
				random.random(),
				'red' )
	for i in range(10):
		leaf( random.randint( -300, -100 ),
				random.randint( -300, -100 ),
				random.random(),
				'orange' )
	for i in range(10):
		leaf( random.randint( -300, -100 ),
				random.randint( -300, -100 ),
				random.random(),
				'yellow' )
					
def foliageRight():
	''' foliage scenery right side of image
			use tree() and leaf() functions defined earlier
			to make a variety of size and color foliage
			using for loops to make multiple'''
	turtle.tracer(False)
	for i in range(5):
		tree( random.randint( 100, 350 ),
				random.randint( -300, -100 ),
				random.randint( 1, 2 ))
	for i in range(10):
		leaf( random.randint( 100, 300 ),
				random.randint( -300, -100 ),
				random.random(),
				'red' )
	for i in range(10):
		leaf( random.randint( 100, 300 ),
				random.randint( -300, -100 ),
				random.random(),
				'orange' )
	for i in range(10):
		leaf( random.randint( 100, 300 ),
				random.randint( -300, -100 ),
				random.random(),
				'yellow' )	
				
def MayflowerHill():
	foliageRight()
	foliageLeft()
	flagpole(0,0,1)

	
		
				
#====================================================================

# Task 5 
# Functions for Outdoor2
# Lighthouse on Water with Wildlife


## functions for landscape() in Outdoor2

def lake( x, y, scale):
	'''draws a lake given location and scale
			use three side by side circles to create lake shape'''
	turtle.tracer(False)
	goto( x, y )
	turtle.begin_fill()
	turtle.color('blue')
	turtle.circle(120*scale)
	turtle.end_fill()
	turtle.begin_fill()
	turtle.color('blue')
	turtle.up()
	turtle.forward(50*scale)
	turtle.down()
	turtle.circle(120*scale)
	turtle.end_fill()
	turtle.begin_fill()
	turtle.color('blue')
	turtle.up()
	turtle.forward(50*scale)
	turtle.down()
	turtle.circle(120*scale)
	turtle.end_fill()
	
def landscape():
	'''this function combines five previous background & landscape functions
			sky(), grass(), lake(), tree(), and star()'''
	sky(0,0,1)
	grass(0,0,1)
	lake(250, -200, 1)
	star(150, 200, 1, 'yellow')
	tree(0,-300,1)
	tree(-100,-250,2)
	tree(-200, -300, 1.5)
	tree(-250, -200, 1)
	tree(100, -250, 1.5)
	tree(325,-230,1)
	tree(250, -300, 1)
	tree(450, -300, 1.5)
	tree(575,-250,1)
	tree(550,-50,2)
	tree(565, -150, 1.5)
	tree(-600, 0, 1)
	tree(-600, -200, 1)
	
	


#--------------------------------	

### functions for wildlife()

def lobster( x, y, scale ):
	'''function to draw lobster using buildingblock(),
			parallelogram(),
			and circle()'''
	turtle.begin_fill()
	turtle.color('red')
	buildingblock(x+250, y-100, 25*scale, 25*scale)
	turtle.end_fill()
	turtle.begin_fill()
	turtle.color('red')
	buildingblock(x+220, y-110, 30*scale, 45*scale)
	turtle.end_fill()
	turtle.begin_fill()
	turtle.color('red')
	buildingblock(x+190, y-125, 35*scale, 75*scale)
	turtle.end_fill()
	turtle.begin_fill()
	turtle.color('red')
	goto(170, -117)
	turtle.circle(30)
	turtle.end_fill()
	# use parallelogram function to make tail rotated 90degrees
	turtle.left(90)
	parallelogram(290, -120, 0.5, 'red')
	turtle.left(120)
	turtle.begin_fill()
	turtle.color('red')
	buildingblock(x+185, y-60, 60*scale, 10*scale)
	turtle.end_fill()
	turtle.begin_fill()
	turtle.color('red')
	buildingblock(x+185, y-170, 60*scale, 10*scale)
	turtle.end_fill()
	turtle.begin_fill()
	turtle.color('red')
	# use circle() and goto() functions to  make claws and eyes
	goto(195, -15)
	turtle.circle(25)
	turtle.end_fill()
	turtle.begin_fill()
	turtle.color('red')
	goto(185, -10)
	turtle.circle(25)
	turtle.end_fill()
	turtle.begin_fill()
	turtle.color('red')
	goto(195, -165)
	turtle.circle(25)
	turtle.end_fill()
	turtle.begin_fill()
	turtle.color('red')
	goto(185, -170)
	turtle.circle(25)
	turtle.end_fill()
	turtle.begin_fill()
	turtle.color('black')
	goto(150, -100)
	turtle.circle(5)
	turtle.end_fill()
	turtle.begin_fill()
	turtle.color('black')
	goto(150, -75)
	turtle.circle(5)
	turtle.end_fill()
	
def moose( x, y, scale ):
	'''function to draw lobster using buildingblock(),
			and circle()'''
	turtle.tracer(False)
	turtle.begin_fill()
	turtle.color('brown')
	buildingblock(x+50, y-200, 10*scale, 20*scale)
	turtle.end_fill()
	turtle.begin_fill()
	turtle.color('brown')
	buildingblock(x-150, y-200, 10*scale, 20*scale)
	turtle.end_fill()
	turtle.begin_fill()
	turtle.color('gray')
	buildingblock(x+45, y-200, 100*scale, 10*scale)
	turtle.end_fill()
	turtle.begin_fill()
	turtle.color('gray')
	buildingblock(x-155, y-200, 100*scale, 10*scale)
	turtle.end_fill()
	turtle.begin_fill()
	turtle.color('brown')
	buildingblock(x+60, y-100, 100*scale, 250*scale)
	turtle.end_fill()
	turtle.begin_fill()
	turtle.color('brown')
	goto(-150,5)
	turtle.circle(50)
	turtle.end_fill()
	turtle.begin_fill()
	turtle.color('brown')
	buildingblock(x-200, y-75, 60*scale, 65*scale)
	turtle.end_fill()
	turtle.begin_fill()
	turtle.color('white')
	goto(-220,10)
	turtle.circle(20)
	turtle.end_fill()
	turtle.begin_fill()
	turtle.color('white')
	goto(-195,10)
	turtle.circle(20)
	turtle.end_fill()
	turtle.begin_fill()
	turtle.color('brown')
	turtle.left(30)
	buildingblock(x-225, y+40, 40*scale, 10*scale)
	turtle.end_fill()
	turtle.begin_fill()
	turtle.color('brown')
	turtle.right(60)
	buildingblock(x-175, y+40, 40*scale, 10*scale)
	turtle.end_fill()
	turtle.begin_fill()
	turtle.color('white')
	goto(-130, 80)
	turtle.circle(30)
	turtle.end_fill()
	turtle.begin_fill()
	turtle.color('white')
	goto(-230, 80)
	turtle.circle(30)
	turtle.end_fill()
	turtle.begin_fill()
	turtle.color('black')
	goto(-235,-60)
	turtle.circle(5)
	turtle.end_fill()
	turtle.begin_fill()
	turtle.color('black')
	goto(-220,-60)
	turtle.circle(5)
	turtle.end_fill()
	turtle.begin_fill()
	turtle.color('black')
	goto(75,5)
	turtle.circle(15)
	turtle.end_fill()
	turtle.begin_fill()
	turtle.color('black')
	goto(-235,0)
	turtle.circle(5)
	turtle.end_fill()
	turtle.begin_fill()
	turtle.color('black')
	goto(-220,0)
	turtle.circle(5)
	turtle.end_fill()
	
	
def wildlife():
	'''this function combines two previous wildlife functions
			lobster() and moose()'''
	lobster(0,0,1)
	moose(0,0,1)
	
#--------------------------------	

### functions for Lighthouse()

def roof( x, y, scale ):
	'''draws a roof given location and scale'''
	goto( x, y )
	turtle.tracer(False)
	turtle.begin_fill()
	turtle.color('blue')
	turtle.forward(200)
	turtle.left(120)
	turtle.forward(200)
	turtle.left(120)
	turtle.forward(200)
	turtle.end_fill()
	turtle.left(120)
	
def lighthouse( x, y, scale ):
	'''draws a lighthouse given location and scale'''
	turtle.tracer(False)
	turtle.begin_fill()
	turtle.color('white')
	buildingblock(x-550, y-325, 200*scale, 325*scale)
	turtle.end_fill()
	turtle.begin_fill()
	turtle.color('red')
	buildingblock(x-550, y+0, 200*scale, 50*scale)
	turtle.end_fill()
	turtle.begin_fill()
	turtle.color('gray')
	buildingblock(x-550, y+50, 200*scale, 70*scale)
	turtle.end_fill()
	turtle.begin_fill()
	turtle.color('white')
	buildingblock(x-525, y+120, 150*scale, 100*scale)
	turtle.end_fill()
	turtle.begin_fill()
	turtle.color('yellow')
	buildingblock(x-488, y+130, 75*scale, 75*scale)
	turtle.end_fill()
	roof( -550, 200, 0.5 )
	
	
	


#====================================================================

# Task 6 = extensions

#====================================================================


# main drawing code section
# used in shapelib.py to test functions


turtle.update()


raw_input('Press enter to continue')
