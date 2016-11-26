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
# Extension2
# change the outdoor scene!

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

def painting( x, y, scale ):
	t.tracer(False)
	t.begin_fill()
	t.color('Brown')
	bsl.buildingblock(x-400*scale, y-75*scale, 250*scale, 250*scale)
	t.end_fill()
	bsl.myscene2(-275, 50,.10)
	t.setheading(0)
	
def window( x, y, scale ):
	t.tracer(False)
	t.begin_fill()
	t.color('White')
	bsl.buildingblock(x+150*scale, y-75*scale, 250*scale, 250*scale)
	t.end_fill()
	
def outsidewindow( x, y, scale):
	t.begin_fill()
	t.color('Green')
	bsl.buildingblock(x+150*scale, y-75*scale, 250*scale, 100*scale)
	t.end_fill()
	t.begin_fill()
	t.color('Light Blue')
	bsl.buildingblock(x+150*scale, y+25*scale, 250*scale, 150*scale)
	t.end_fill()
	bsl.star(x+350*scale, y+125*scale, .25*scale, 'True', 'orange')
	
def windowpane( x, y, scale ):
	t.begin_fill()
	t.color('Gray')
	bsl.buildingblock(x+150*scale, y+40*scale, 250*scale, 10*scale)
	t.end_fill()
	t.begin_fill()
	t.color('Gray')
	bsl.buildingblock(x+275*scale, y-75*scale, 10*scale, 250*scale)
	t.end_fill()
	

def outsidewindownight( x, y, scale):
	t.begin_fill()
	t.color('Dark Blue')
	bsl.buildingblock(x+150*scale, y-75*scale, 250*scale, 100*scale)
	t.end_fill()
	t.begin_fill()
	t.color('Black')
	bsl.buildingblock(x+150*scale, y+25*scale, 250*scale, 150*scale)
	t.end_fill()
	bsl.star(x+350*scale, y+125*scale, .10*scale, 'True', 'yellow')
	bsl.star(x+250*scale, y+75*scale, .10*scale, 'True', 'yellow')
	bsl.star(x+275*scale, y+100*scale, .10*scale, 'True', 'yellow')
	bsl.star(x+300*scale, y+125*scale, .10*scale, 'True', 'yellow')
	bsl.star(x+250*scale, y+125*scale, .10*scale, 'True', 'white')
	bsl.star(x+350*scale, y+65*scale, .10*scale, 'True', 'white')
	bsl.star(x+300*scale, y+75*scale, .10*scale, 'True', 'yellow')
	t.begin_fill()
	t.color('Gray')
	bsl.goto(x+200*scale, y+75*scale)
	t.circle(40)
	t.end_fill()
	
def outsidewindowmorning( x, y, scale):
	t.begin_fill()
	t.color('Green')
	bsl.buildingblock(x+150*scale, y-75*scale, 250*scale, 100*scale)
	t.end_fill()
	t.begin_fill()
	t.color('Light Blue')
	bsl.buildingblock(x+150*scale, y+25*scale, 250*scale, 150*scale)
	t.end_fill()
	bsl.star(x+250*scale, y+70*scale, .6*scale, 'True', 'Red')
	bsl.cloud(x+175*scale, y+125*scale, 0.25*scale, 'white')
	bsl.cloud(x+200*scale, y+75*scale, 0.3*scale, 'white')
	bsl.cloud(x+350*scale, y+120*scale, 0.3*scale, 'white')
	bsl.cloud(x+275*scale, y+100*scale, 0.4*scale, 'white')
	bsl.cloud(x+350*scale, y+50*scale, 0.25*scale, 'white')
	
def invasion( x, y, scale ):
	t.begin_fill()
	t.color('Purple')
	bsl.buildingblock(x+150*scale, y-75*scale, 250*scale, 100*scale)
	t.end_fill()
	t.begin_fill()
	t.color('Red')
	bsl.buildingblock(x+150*scale, y+25*scale, 250*scale, 150*scale)
	t.end_fill()
	bsl.star(x+350*scale, y+125*scale, .25*scale, 'True', 'Black')
	bsl.goto(200*scale, 100*scale)
	t.begin_fill()
	t.color("Yellow")
	t.circle(25)
	t.end_fill()
	bsl.goto(200*scale, 110*scale)
	t.begin_fill()
	t.color("White")
	t.circle(15)
	t.end_fill()
	bsl.goto(200*scale, 120*scale)
	t.begin_fill()
	t.color("Orange")
	t.circle(5)
	t.end_fill()
	t.setheading(-30)
	t.begin_fill()
	t.color('Green')
	bsl.buildingblock(x+200*scale, y+95*scale, 20*scale, 5*scale)
	t.end_fill()
	t.setheading(0)
	t.setheading(-30)
	t.begin_fill()
	t.color('Green')
	bsl.buildingblock(x+225*scale, y+75*scale, 20*scale, 5*scale)
	t.end_fill()
	t.setheading(0)
	t.setheading(-30)
	t.begin_fill()
	t.color('Green')
	bsl.buildingblock(x+230*scale, y+110*scale, 20*scale, 5*scale)
	t.end_fill()
	t.setheading(0)
	t.setheading(-30)
	t.begin_fill()
	t.color('Green')
	bsl.buildingblock(x+250*scale, y+100*scale, 20*scale, 5*scale)
	t.end_fill()
	t.setheading(0)
	
	
def museum2( x, y, scale, time):		
	wall(x+0*scale, y+0*scale, 1*scale)
	ceiling(x+0*scale, y+0*scale, 1*scale)
	floor(x+0*scale, y+0*scale, 1*scale)
	painting(x+0*scale, y+0*scale, 1*scale)
	window(x+0*scale, y+0*scale, 1*scale)
	if time == "Night":
		outsidewindownight(x+0*scale, y+0*scale, 1*scale)
	elif time == "Invasion":
		invasion(x+0*scale, y+0*scale, 1*scale)
	else:
		outsidewindowmorning(x+0*scale, y+0*scale, 1*scale)
	windowpane(x+0*scale, y+0*scale, 1*scale)
	
museum2(0,0,1, sys.argv[1])



raw_input("Hit enter to continue")