# Tony Karalekas
# Spring 2015
# CS 151 Project 3

#====================================================================

# import different modules 
import turtle as t
import random
import shapelib 

#----------------------------
# TASK 1

# same goto() function from Lab2
def goto( x, y ):
	'''sends the turtle to location (x,y) without drawing'''
	print 'Sending turtle to' , x,y
	t.up()
	t.goto( x, y )
	t.down()

# block function from lab2 with looping and more parameters
def block( x, y, width, height, fill, color ):
	goto( x, y )
	
	print 'block(): drawing block of size', width, height
	# tell the turtle to go foward by width
	# tell the turtle to turn left by 90 degrees
	# tell the turtle to go forward by height
	# tell the turtle to turn left by 90 degrees
	# repeat the above 4 commands
	
	# if the parameter fill is true then do this
	if fill == "True":
		''' draw a block at position (x,y) with the
			given width and height, and fill with 
			the color '''
		t.begin_fill()
		t.color(color)
		for i in range(2):
			t.forward(width)
			t.left(90)
			t.forward(height)
			t.left(90)	
		t.end_fill()
	# if the parameter fill is false then do this
	else:
		''' draw a block at position (x,y) with the
			given width and height, and fill with 
			the color '''
		for i in range(2):
			t.forward(width)
			t.left(90)
			t.forward(height)
			t.left(90)	
			
#====================================================================
			
# TASK 2

# simplify shapes from lab2
# simple shape cross() from lab2 now with loops and if statements

def cross( x, y, scale, fill, color ):
	'''draws a cross given location, scale, and color'''
	goto( x, y )
	
	if fill == "True":
		'''if the scale is 1, and fill == True
			then this function will draw a cross 
			with its left point at (x,y) and
			will have lengths of 50 and widths of 15
			and filled with the color given'''
		t.begin_fill()
		t.color(color)
		for i in range(4):
			t.forward(50*scale)
			t.right(90)
			t.forward(50*scale)
			t.left(90)
			t.forward(15*scale)
			t.left(90)
		t.end_fill()
	else: 
		'''if the scale is 1, and fill == False
			then this function will draw a cross 
			with its left point at (x,y) and
			will have lengths of 50 and widths of 15
			and with no color fill'''
		for i in range(4):
			t.forward(50*scale)
			t.right(90)
			t.forward(50*scale)
			t.left(90)
			t.forward(15*scale)
			t.left(90)
			
def parallelogram( x, y, scale, color ):
	'''draws a parallelogram given location, scale, and color'''
	goto( x, y )
	t.begin_fill()
	t.color(color)
	t.forward(100*scale)
	t.left(60)
	t.forward(50*scale)
	t.left(120)
	t.forward(100*scale)
	t.left(60)
	t.forward(50*scale)
	t.end_fill() 
	
	
#----------------------------

# simple shape cross() from lab2 now with loops and if statements
			
def star( x, y, scale, fill, color ):
	'''draws a star given location, scale, and color'''
	goto( x, y )
	
	if fill == "True":
		'''if the scale is 1, and fill == True
			then this function will draw a star 
			with its left point at (x,y) and
			will have star ray lengths of 50
			and filled with the color given'''
		t.begin_fill()
		t.color(color)
		for i in range(10):
			t.forward(50*scale)
			t.right(108)
			t.forward(50*scale)
			t.left(144)
		t.end_fill()
	else: 
		'''if the scale is 1, and fill == False
			then this function will draw a star 
			with its left point at (x,y) and
			will have star ray lengths of 50
			and with no color fill'''
		t.begin_fill()
		for i in range(10):
			t.forward(50*scale)
			t.right(108)
			t.forward(50*scale)
			t.left(144)
			
#====================================================================

# TASK 3

# simplify aggregate shapes from lab2

'''notes from meeting with prof taylor about two argument list for loops'''
# dists = [25, 25, 25, 25]
# turns = [150, -150, 150, -150]
# 
# for i in range( len(dists)):
# 	t.forward( dists[i]*scale)
# 	t.left( turns[i])

# leaf() function rewritten with multiple argument for loop		
def leaf( x, y, scale, fill, color ):
	t.tracer(False)
	'''draws a leaf given location and scale'''
	goto( x, y )
	dists = [ 8.33, 3.33, 15, 5, 15, 15, 5, 15, 3.33, 8.33, 10, 10, 10, 8.33]
	turns = [ -30, 120, -105, 110, -95, 150, -95, 110, -105, 120, 60, 30, 180, 75]
	if fill == "True":
		t.begin_fill()
		t.color(color)
		for i in range( len(dists)):
			t.left( turns[i])
			t.forward( dists[i]*scale)
		t.end_fill()
	else:
		t.begin_fill()
		for i in range( len(dists)):
			t.left( turns[i])
			t.forward( dists[i]*scale)
	
# tree() function rewritten with multiple argument for loop	
def tree( x, y, scale ):
	t.tracer(False)
	'''draws a leaf given location and scale'''
	goto( x, y )
	t.setheading(0)
	dists1 = [ 25, 25, 20, 30, 30, 20, 25, 30]
	turns1 = [ 150, -150, 150, 60, 150, -150, 150, 0]
	t.begin_fill()
	t.color('dark green')
	for i in range( len(dists1)):	
		t.forward( dists1[i]*scale)
		t.left( turns1[i])
	t.end_fill()
	dists2 = [ 15, 5, 15, 5 ]
	turns2 = [ 90, 90, 90, 90 ]
	goto( x, y )
	t.begin_fill()
	t.color('brown')
	for i in range( len(dists2)):	
		t.right( turns2[i])
		t.forward( dists2[i]*scale)
	t.end_fill()


#======================================================================

# Task 4
# For this task I decided to take all my code from project2 
# and scale BOTH of my mMine outdoor images
# outdoors1() and outdoors2() become myscene1() and myscene2()



# Functions for Outdoor1
# Mayflower Hill and Miller Library 
# to become myscene1()
	
	
### functions for background() for Outdoor1
''' ALL NOW SCALE AND POSITION DEPENDENT '''

def cloud( x, y, scale, color):
	'''draws a cloud given location and scale'''
	goto( x, y )
	t.begin_fill()
	t.color(color)
	t.circle(50*scale)
	t.end_fill()
	t.begin_fill()
	t.color(color)
	t.up()
	t.forward(25*scale)
	t.down()
	t.circle(50*scale)
	t.end_fill()
	t.begin_fill()
	t.color(color)
	t.up()
	t.forward(35*scale)
	t.down()
	t.circle(50*scale)
	t.end_fill()
	t.begin_fill()
	t.color(color)
	t.up()
	t.forward(25*scale)
	t.down()
	t.circle(50*scale)
	t.end_fill()
	t.begin_fill()
	t.color(color)
	t.up()
	t.forward(25*scale)
	t.down()
	t.end_fill()

def sky( x, y, scale ):
	'''draws a huge blue square given location and scale'''
	t.tracer(False)
	t.begin_fill()
	t.color('light blue')
	buildingblock(x-1000*scale, y+0*scale, 2000*scale, 1075*scale)
	t.end_fill()

def grass( x, y, scale ):
	'''draws a huge blue square given location and scale'''
	t.tracer(False)
	t.begin_fill()
	t.color('green')
	buildingblock(x-1000*scale, y-1000*scale, 2000*scale, 1075*scale)
	t.end_fill()
	
def skyobjects( x, y, scale ):
	'''puts all of the objects in sky functions togehter'''
	t.tracer(False)
	star(x-300*scale, y+225*scale, 1*scale, 'True', 'orange')
	cloud(x+250*scale, y+200*scale, 1*scale, 'gray')
	cloud(x+175*scale, y+125*scale, 0.5*scale, 'gray')
	cloud(x+125*scale, y+215*scale, 0.25*scale, 'gray')

def background( x, y, scale ):
	sky(x+0*scale, y+0*scale, 1*scale)
	grass(x+0*scale, y+0*scale, 1*scale)
	skyobjects(x+0*scale, y+0*scale, 1*scale)
	
#--------------------------------

### functions for MillerLibrary() in outdoors1
''' ALL NOW SCALE AND POSITION DEPENDENT '''
	
def letterC( x, y, scale ):
	'''draws a letter C given location and scale'''
	goto(0*scale,0*scale)
	t.tracer(False)
	t.begin_fill()
	t.color('blue')
	buildingblock(x+25*scale, y+200*scale, 50*scale, 10*scale)
	t.end_fill()
	t.begin_fill()
	t.color('blue')
	buildingblock(x-25*scale, y+225*scale, 10*scale, 60*scale)
	t.end_fill()
	t.begin_fill()
	t.color('blue')
	buildingblock(x+25*scale, y+225*scale, 50*scale, 10*scale)
	t.end_fill()
		
def buildingblock( x, y, width, height ):
# same code in block() function from lab 2
	'''building blocks for structures given location and scale'''
	goto( x, y )
	for i in range(2):
		t.forward(width)
		t.left(90)
		t.forward(height)
		t.left(90)
	
def MillerLibrary( x, y, scale ):
	''' Miller Library using buildingblocks()'''
	t.tracer(False)
	t.color('black')
	t.begin_fill()
	t.color('black')
	buildingblock(x-150*scale, y+0*scale, 300*scale, 100*scale)
	t.end_fill()
	t.begin_fill()
	t.color('gray')
	buildingblock(x-250*scale, y+0*scale, 100*scale, 50*scale)
	t.end_fill()
	t.begin_fill()
	t.color('gray')
	buildingblock(x+150*scale, y+0*scale, 100*scale, 50*scale)
	t.end_fill()
	t.begin_fill()
	t.color('white')
	buildingblock(x-125*scale, y-25*scale, 250*scale, 25*scale)
	t.end_fill()
	t.begin_fill()
	t.color('gray')
	buildingblock(x-100*scale, y-50*scale, 200*scale, 25*scale)
	t.begin_fill()
	t.color('white')
	buildingblock(x-75*scale, y-75*scale, 150*scale, 25*scale)
	t.end_fill()
	t.begin_fill()
	t.color('gray')
	buildingblock(x-50*scale, y-100*scale, 100*scale, 25*scale)
	t.end_fill()
	t.begin_fill()
	t.color('gray')
	buildingblock(x-100*scale, y+100*scale, 200*scale, 50*scale)
	t.end_fill()
	t.begin_fill()
	t.color('white')
	buildingblock(x-25*scale, y+150*scale, 50*scale, 100*scale)
	t.end_fill()
	t.begin_fill()
	t.color('gray')
	buildingblock(x-5*scale, y+250*scale, 10*scale, 40*scale)
	t.end_fill()
	t.begin_fill()
	t.color('blue')
	buildingblock(x-5*scale, y+290*scale, 10*scale, 10*scale)
	t.end_fill()
	t.begin_fill()
	t.color('blue')
	buildingblock(x-100*scale, y+0*scale, 15*scale, 100*scale)
	t.end_fill()
	t.begin_fill()
	t.color('blue')
	buildingblock(x-50*scale, y+0*scale, 15*scale, 100*scale)
	t.end_fill()
	t.begin_fill()
	t.color('blue')
	buildingblock(x-7.5*scale, y+0*scale, 15*scale, 100*scale)
	t.end_fill()
	t.begin_fill()
	t.color('blue')
	buildingblock(x+85*scale, y+0*scale, 15*scale, 100*scale)
	t.end_fill()
	t.begin_fill()
	t.color('blue')
	buildingblock(x+35*scale, y+0*scale, 15*scale, 100*scale)
	t.end_fill()
	# add decorations to the library
	# blue crosses and blue C
	cross(x-80*scale, y+125*scale, 0.25*scale*scale, 'True', 'blue')
	cross(x+0*scale, y+140*scale, 0.25*scale*scale, 'True', 'blue')
	cross(x+80*scale, y+125*scale, 0.25*scale*scale, 'True', 'blue')
	t.up()
	t.left(90)
	t.down()
	letterC(x+0*scale, y+0*scale, 0.5*scale)
	
#--------------------------------	

### functions for MayflowerHill() in outdoors1
''' ALL NOW SCALE AND POSITION DEPENDENT '''

def flagpole( x, y, scale ):
	'''draws a flagpole given location and scale'''
	t.setheading(0)
	t.begin_fill()
	t.color('gray')
	buildingblock(x-25*scale, y-350*scale, 50*scale, 50*scale)
	t.end_fill()
	t.begin_fill()
	t.color('gray')
	buildingblock(x-15*scale, y-300*scale, 30*scale, 25*scale)
	t.end_fill()
	t.begin_fill()
	t.color('white')
	buildingblock(x-5*scale, y-275*scale, 10*scale, 100*scale)
	t.end_fill()
	t.begin_fill()
	t.color('blue')
	buildingblock(x-5*scale, y-175*scale, 50*scale, 25*scale)
	t.end_fill()

def foliageLeft( x, y, scale):
	''' foliage scenery left side of image
			use tree() and leaf() functions defined earlier
			to make a variety of size and color foliage
			using for loops to make multiple'''
	t.tracer(False)
	for i in range(5):
		tree( x+random.randint( -300, -100 )*scale,
				y+random.randint( -300, -100 )*scale,
				random.randint( 1, 2 )*scale)
	for i in range(10):
		leaf( x+random.randint( -300, -100 )*scale,
				y+random.randint( -300, -100 )*scale,
				random.random()*scale,
				'red' )
	for i in range(10):
		leaf( x+random.randint( -300, -100 )*scale,
				y+random.randint( -300, -100 )*scale,
				random.random()*scale,
				'orange' )
	for i in range(10):
		leaf( x+random.randint( -300, -100 )*scale,
				y+random.randint( -300, -100 )*scale,
				random.random()*scale,
				'yellow' )
					
def foliageRight( x, y, scale):
	''' foliage scenery right side of image
			use tree() and leaf() functions defined earlier
			to make a variety of size and color foliage
			using for loops to make multiple'''
	t.tracer(False)
	for i in range(5):
		tree( x+random.randint( 100, 350 )*scale,
				y+random.randint( -300, -100 )*scale,
				random.randint( 1, 2 )*scale)
	for i in range(10):
		leaf( x+random.randint( 100, 300 )*scale,
				y+random.randint( -300, -100 )*scale,
				random.random()*scale,
				'red' )
	for i in range(10):
		leaf( x+random.randint( 100, 300 ),
				y+random.randint( -300, -100 ),
				random.random()*scale,
				'orange' )
	for i in range(10):
		leaf( x+random.randint( 100, 300 )*scale,
				y+random.randint( -300, -100 )*scale,
				random.random()*scale,
				'yellow' )	
				
def MayflowerHill( x, y, scale ):
	foliageRight(x+0*scale, y+0*scale, 1*scale)
	foliageLeft(x+0*scale, y+0*scale, 1*scale)
	flagpole(x+0*scale, y+0*scale, 1*scale)
	
#-------------------------------------------
	

# myscene1() function takes my second outdoor image from project2
# and allows me to scale and position the entire image

'''This is my new function. It is basically the same as Outdoors1
	but now it allows me to scale and position the entire image'''

def myscene1( x, y, scale ):
	'''scale and position dependent function of outdoors1 in project2'''
	background(x+0*scale, y+0*scale, 1*scale)
	MillerLibrary(x+0*scale, y+0*scale, 1*scale)
	MayflowerHill(x+0*scale, y+0*scale, 1*scale)

				
#====================================================================

# Task 4 CONTINUED

# Functions for Outdoor2
# Lighthouse on Water with Wildlife
# to become myscene2()


## functions for landscape() in Outdoor2
''' ALL NOW SCALE AND POSITION DEPENDENT '''


def lake( x, y, scale):
	'''draws a lake given location and scale
			use three side by side circles to create lake shape'''
	t.tracer(False)
	goto( x, y )
	t.begin_fill()
	t.color('blue')
	t.circle(120*scale)
	t.end_fill()
	t.begin_fill()
	t.color('blue')
	t.up()
	t.forward(50*scale)
	t.down()
	t.circle(120*scale)
	t.end_fill()
	t.begin_fill()
	t.color('blue')
	t.up()
	t.forward(50*scale)
	t.down()
	t.circle(120*scale)
	t.end_fill()
	
def landscape( x, y, scale ):
	'''this function combines five previous background & landscape functions
			sky(), grass(), lake(), tree(), and star()'''
	sky(x+0*scale,y+0*scale,1*scale)
	grass(x+0*scale,y+0*scale,1*scale)
	lake(x+250*scale, y-200*scale, 1*scale)
	star(x+150*scale, y+200*scale, 1*scale, 'True', 'yellow')
	tree(x+0*scale,y-300*scale,1*scale)
	tree(x-100*scale,y-250*scale,2*scale)
	tree(x-200*scale, y-300*scale, 1.5*scale)
	tree(x-250*scale, y-200*scale, 1*scale)
	tree(x+100*scale, y-250*scale, 1.5*scale)
	tree(x+325*scale,y-230*scale,1*scale)
	tree(x+250*scale, y-300*scale, 1*scale)
	tree(x+450*scale, y-300*scale, 1.5*scale)
	tree(x+575*scale,y-250*scale,1*scale)
	tree(x+550*scale,y-50,2*scale)
	tree(x+565*scale, y-150*scale, 1.5*scale)
	tree(x-600*scale, y+0*scale, 1*scale)
	tree(x-600*scale, y-200*scale, 1*scale)

#--------------------------------	

### functions for wildlife() in outdoors2
''' ALL NOW SCALE AND POSITION DEPENDENT '''


def lobster( x, y, scale ):
	'''function to draw lobster using buildingblock(),
			parallelogram(),
			and circle()'''
	t.begin_fill()
	t.color('red')
	buildingblock(x+250*scale, y-100*scale, 25*scale, 25*scale)
	t.end_fill()
	t.begin_fill()
	t.color('red')
	buildingblock(x+220*scale, y-110*scale, 30*scale, 45*scale)
	t.end_fill()
	t.begin_fill()
	t.color('red')
	buildingblock(x+190*scale, y-125*scale, 35*scale, 75*scale)
	t.end_fill()
	t.begin_fill()
	t.color('red')
	goto(x+170*scale, y-117*scale)
	t.circle(30*scale)
	t.end_fill()
	# use parallelogram function to make tail rotated 90degrees
	t.left(90)
	parallelogram(x+290*scale, y-120*scale, 0.5*scale, 'red')
	t.left(120)
	t.begin_fill()
	t.color('red')
	buildingblock(x+185*scale, y-60*scale, 60*scale, 10*scale)
	t.end_fill()
	t.begin_fill()
	t.color('red')
	buildingblock(x+185*scale, y-170*scale, 60*scale, 10*scale)
	t.end_fill()
	t.begin_fill()
	t.color('red')
	# use circle() and goto() functions to  make claws and eyes
	goto(x+195*scale, y-15*scale)
	t.circle(25*scale)
	t.end_fill()
	t.begin_fill()
	t.color('red')
	goto(x+185*scale, y-10*scale)
	t.circle(25*scale)
	t.end_fill()
	t.begin_fill()
	t.color('red')
	goto(x+195*scale, y-165*scale)
	t.circle(25*scale)
	t.end_fill()
	t.begin_fill()
	t.color('red')
	goto(x+185*scale, y-170*scale)
	t.circle(25*scale)
	t.end_fill()
	t.begin_fill()
	t.color('black')
	goto(x+150*scale, y-100*scale)
	t.circle(5*scale)
	t.end_fill()
	t.begin_fill()
	t.color('black')
	goto(x+150*scale, y-75*scale)
	t.circle(5*scale)
	t.end_fill()
	
def moose( x, y, scale ):
	'''function to draw lobster using buildingblock(),
			and circle()'''
	t.tracer(False)
	t.begin_fill()
	t.color('brown')
	buildingblock(x+50*scale, y-200*scale, 10*scale, 20*scale)
	t.end_fill()
	t.begin_fill()
	t.color('brown')
	buildingblock(x-150*scale, y-200*scale, 10*scale, 20*scale)
	t.end_fill()
	t.begin_fill()
	t.color('gray')
	buildingblock(x+45*scale, y-200*scale, 100*scale, 10*scale)
	t.end_fill()
	t.begin_fill()
	t.color('gray')
	buildingblock(x-155*scale, y-200*scale, 100*scale, 10*scale)
	t.end_fill()
	t.begin_fill()
	t.color('brown')
	buildingblock(x+60*scale, y-100*scale, 100*scale, 250*scale)
	t.end_fill()
	t.begin_fill()
	t.color('brown')
	goto(x-150*scale,y+5*scale)
	t.circle(50*scale)
	t.end_fill()
	t.begin_fill()
	t.color('brown')
	buildingblock(x-200*scale, y-75*scale, 60*scale, 65*scale)
	t.end_fill()
	t.begin_fill()
	t.color('white')
	goto(x-220*scale,y+10*scale)
	t.circle(20*scale)
	t.end_fill()
	t.begin_fill()
	t.color('white')
	goto(x-195*scale,y+10*scale)
	t.circle(20*scale)
	t.end_fill()
	t.begin_fill()
	t.color('brown')
	t.left(30)
	buildingblock(x-225*scale, y+40*scale, 40*scale, 10*scale)
	t.end_fill()
	t.begin_fill()
	t.color('brown')
	t.right(60)
	buildingblock(x-175*scale, y+40*scale, 40*scale, 10*scale)
	t.end_fill()
	t.begin_fill()
	t.color('white')
	goto(x-130*scale, y+80*scale)
	t.circle(30*scale)
	t.end_fill()
	t.begin_fill()
	t.color('white')
	goto(x-230*scale, y+80*scale)
	t.circle(30*scale)
	t.end_fill()
	t.begin_fill()
	t.color('black')
	goto(x-235*scale,y-60*scale)
	t.circle(5*scale)
	t.end_fill()
	t.begin_fill()
	t.color('black')
	goto(x-220*scale,y-60*scale)
	t.circle(5*scale)
	t.end_fill()
	t.begin_fill()
	t.color('black')
	goto(x+75*scale,y+5*scale)
	t.circle(15*scale)
	t.end_fill()
	t.begin_fill()
	t.color('black')
	goto(x-235*scale,y+0*scale)
	t.circle(5*scale)
	t.end_fill()
	t.begin_fill()
	t.color('black')
	goto(x-220*scale,y+0*scale)
	t.circle(5*scale)
	t.end_fill()

def wildlife( x, y, scale):
	'''this function combines two previous wildlife functions
			lobster() and moose()'''
	lobster(x+0,y+0,1*scale)
	moose(x+0,y+0,1*scale)
	
#--------------------------------	

### functions for Lighthouse() in outdoors2
''' ALL NOW SCALE AND POSITION DEPENDENT '''


def roof( x, y, scale ):
	'''draws a roof given location and scale'''
	goto( x, y )
	t.tracer(False)
	t.begin_fill()
	t.color('blue')
	t.forward(200*scale)
	t.left(120)
	t.forward(200*scale)
	t.left(120)
	t.forward(200*scale)
	t.end_fill()
	t.left(120)
	
def lighthouse( x, y, scale ):
	'''draws a lighthouse given location and scale'''
	t.tracer(False)
	t.begin_fill()
	t.color('white')
	buildingblock(x-550*scale, y-325*scale, 200*scale, 325*scale)
	t.end_fill()
	t.begin_fill()
	t.color('red')
	buildingblock(x-550*scale, y+0*scale, 200*scale, 50*scale)
	t.end_fill()
	t.begin_fill()
	t.color('gray')
	buildingblock(x-550*scale, y+50*scale, 200*scale, 70*scale)
	t.end_fill()
	t.begin_fill()
	t.color('white')
	buildingblock(x-525*scale, y+120*scale, 150*scale, 100*scale)
	t.end_fill()
	t.begin_fill()
	t.color('yellow')
	buildingblock(x-488*scale, y+130*scale, 75*scale, 75*scale)
	t.end_fill()
	roof( x-500*scale, y+225*scale, 0.5*scale )
	
#---------------------------------

# myscene() function takes my second outdoor image from project2
# and allows me to scale and position the entire image
'''This is my new function. It is basically the same as Outdoors2
	but now it allows me to scale and position the entire image'''

def myscene2( x, y, scale ):
	'''scale and position dependent function of outdoors2 in project2'''
	landscape(x+0*scale, y+0*scale, 1*scale)
	lighthouse(x+0*scale, y+0*scale, 1*scale)
	wildlife(x+0*scale, y+0*scale, 1*scale)


#====================================================================
#====================================================================


# main drawing code section
# used in better_shapelib.py to test functions





raw_input('Press enter to continue')














#====================================================================

# TASK 4

# Functions for Outdoor2 from Lab2
# Lighthouse on Water with Wildlife






# dists = [25, 25, 25, 25]
# turns = [150, -150, 150, -150]
# 
# for i in range( len(dists)):
# 	t.forward( dists[i]*scale)
# 	t.left( turns[i])