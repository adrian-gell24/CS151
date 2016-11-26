# Tony Karalekas
# Spring 2015
# CS 151 Project 2 Extension2

#====================================================================
import turtle
 
import random
 
import shapelib

def ColbyApocalypse( x, y, scale ):
	shapelib.background()
	''' Miller Library using buildingblocks()'''
	turtle.tracer(False)
	turtle.color('black')
	turtle.begin_fill()
	turtle.color('black')
	shapelib.buildingblock(x-150, y+0, 300*scale, 100*scale)
	turtle.end_fill()
	turtle.begin_fill()
	turtle.color('gray')
	shapelib.buildingblock(x-250, y+0, 100*scale, 50*scale)
	turtle.end_fill()
	turtle.begin_fill()
	turtle.color('gray')
	shapelib.buildingblock(x+150, y+0, 100*scale, 50*scale)
	turtle.end_fill()
	turtle.begin_fill()
	turtle.color('gray')
	shapelib.buildingblock(x-125, y-25, 250*scale, 25*scale)
	turtle.end_fill()
	turtle.begin_fill()
	turtle.color('gray')
	shapelib.buildingblock(x-100, y-50, 200*scale, 25*scale)
	turtle.begin_fill()
	turtle.color('brown')
	shapelib.buildingblock(x-75, y-75, 150*scale, 25*scale)
	turtle.end_fill()
	turtle.begin_fill()
	turtle.color('brown')
	shapelib.buildingblock(x-50, y-100, 100*scale, 25*scale)
	turtle.end_fill()
	turtle.begin_fill()
	turtle.color('gray')
	shapelib.buildingblock(x-100, y+100, 200*scale, 50*scale)
	turtle.end_fill()
	turtle.begin_fill()
	turtle.color('black')
	shapelib.buildingblock(x-25, y+150, 50*scale, 100*scale)
	turtle.end_fill()
	turtle.begin_fill()
	turtle.color('gray')
	shapelib.buildingblock(x-5, y+250, 10*scale, 40*scale)
	turtle.end_fill()
	turtle.begin_fill()
	turtle.color('black')
	shapelib.buildingblock(x-5, y+290, 10*scale, 10*scale)
	turtle.end_fill()
	turtle.begin_fill()
	turtle.color('gray')
	shapelib.buildingblock(x-100, y+0, 15*scale, 100*scale)
	turtle.end_fill()
	turtle.begin_fill()
	turtle.color('brown')
	shapelib.buildingblock(x-50, y+0, 15*scale, 100*scale)
	turtle.end_fill()
	turtle.begin_fill()
	turtle.color('gray')
	shapelib.buildingblock(x-7.5, y+0, 15*scale, 100*scale)
	turtle.end_fill()
	turtle.begin_fill()
	turtle.color('brown')
	shapelib.buildingblock(x+85, y+0, 15*scale, 100*scale)
	turtle.end_fill()
	turtle.begin_fill()
	turtle.color('brown')
	shapelib.buildingblock(x+35, y+0, 15*scale, 100*scale)
	turtle.end_fill()
	# add decorations to the library
	# blue crosses and blue C
	shapelib.cross(x-80, y+125, 0.25*scale, 'black')
	shapelib.cross(x+0, y+140, 0.25*scale, 'black')
	shapelib.cross(x+80, y+125, 0.25*scale, 'black')
	for i in range(100):
		shapelib.tree( random.randint( -500, 500 ),
				random.randint( -300, 0 ),
				random.randint( 1, 2 ))
	shapelib.star( -250, 240, 0.5, 'black')
def ghosts():
	for i in range(10):
		ghost(random.randint( -500, 500 ),
				random.randint( -300, 0 ))
	
def ghost( x, y ):
	shapelib.goto(x,y)
	turtle.setheading(0)
	turtle.begin_fill()
	turtle.color('white')
	turtle.circle(50)
	turtle.end_fill
	turtle.up()
	turtle.left(90)
	turtle.forward(25)
	turtle.down()
	turtle.begin_fill()
	turtle.color('red')
	turtle.circle(25)
	turtle.end_fill
	turtle.begin_fill()
	turtle.color('red')
	turtle.circle(25)
	turtle.end_fill


				
				
turtle.update()

ColbyApocalypse(0,0,1) 
shapelib.lobster(0,0,1)
ghosts()


	

raw_input('Press enter to continue')