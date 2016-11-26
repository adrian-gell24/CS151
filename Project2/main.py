# Tony Karalekas
# Spring 2015
# CS 151 Project 2

#====================================================================


import turtle
import shapelib

def outdoors1():
	shapelib.background()
	shapelib.MillerLibrary(0,0,1)
	shapelib.MayflowerHill()
	
	

def outdoors2():
	shapelib.landscape()
	shapelib.lighthouse(0,0,1)
	shapelib.wildlife()
	
	
turtle.update()

outdoors2()


raw_input('Press enter to continue')

