# Tony Karalekas
# Spring 2015
# CS 151 Project 3

#====================================================================

# import different modules 
import turtle as t
import random
import better_shapelib as bsl
import sys

#---------------------------------
# Extension1
# hang both of my images in the museum!

# copied and pasted some code from taskII.py file

def wall( x, y, scale ):
	t.tracer(False)
	t.begin_fill()
	t.color('Beige')
	bsl.buildingblock(x-1000*scale, y-1000*scale, 2000*scale, 2000*scale)
	t.end_fill()

def ceiling( x, y, scale ):
	t.tracer(False)
	position = [-600, -550, -500, -450, -400,-350,-300, -250, -200, -150, -100, -50, 0,
				 50, 100, 150, 200, 250, 300, 350, 400, 450, 500, 550] 
	for i in range(len(position)):
		bsl.star(x+position[i]*scale, y+225*scale, .5*scale, 'True', 'blue')

def floor( x, y, scale ):
	t.tracer(False)
	position1 = [-600, -500, -400, -300, -200, -100, 0, 100, 200, 300, 400, 500]
	position2 = [-550, -450, -350, -250, -150, -50, 50, 150, 250, 350, 450,  550]
	for i in range(len(position1)):
		t.begin_fill()
		t.color('Black')
		bsl.buildingblock(x+position1[i]*scale, y-300*scale, 50*scale, 50*scale)
		t.end_fill()
	for i in range(len(position1)):
		t.begin_fill()
		t.color('Gold')
		bsl.buildingblock(x+position2[i]*scale, y-300*scale, 50*scale, 50*scale)
		t.end_fill()
	for i in range(len(position1)):
		t.begin_fill()
		t.color('Gold')
		bsl.buildingblock(x+position1[i]*scale, y-250*scale, 50*scale, 50*scale)
		t.end_fill()
	for i in range(len(position1)):
		t.begin_fill()
		t.color('Black')
		bsl.buildingblock(x+position2[i]*scale, y-250*scale, 50*scale, 50*scale)
		t.end_fill()
	for i in range(len(position1)):
		t.begin_fill()
		t.color('Black')
		bsl.buildingblock(x+position1[i]*scale, y-200*scale, 50*scale, 50*scale)
		t.end_fill()
	for i in range(len(position1)):
		t.begin_fill()
		t.color('Gold')
		bsl.buildingblock(x+position2[i]*scale, y-200*scale, 50*scale, 50*scale)
		t.end_fill()

def painting1( x, y, scale ):
	t.tracer(False)
	t.begin_fill()
	t.color('Brown')
	bsl.buildingblock(x-400*scale, y-75*scale, 250*scale, 250*scale)
	t.end_fill()
	bsl.myscene2(-275, 50,.10)
	t.setheading(0)

def painting2( x, y, scale ):
	t.tracer(False)
	t.begin_fill()
	t.color('Brown')
	bsl.buildingblock(x+150*scale, y-75*scale, 250*scale, 250*scale)
	t.end_fill()
	bsl.myscene1(275, 50,.10)
	t.setheading(0)
	
def museum( x, y, scale):		
	wall(x+0*scale, y+0*scale, 1*scale)
	ceiling(x+0*scale, y+0*scale, 1*scale)
	floor(x+0*scale, y+0*scale, 1*scale)
	painting1(x+0*scale, y+0*scale, 1*scale)
	painting2(x+0*scale, y+0*scale, 1*scale)
	
museum(0,0,1)
	
raw_input('Hit enter to continue')
	
	
	