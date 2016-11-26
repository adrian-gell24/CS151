# Tony Karalekas
# Spring 2015
# CS 151 Project 10
#
# turtle_interpreter.py version 4
#---------------------------------------------
#
# The purpose of this file is to convert a string
# into an image using simple turtle commands 
#
#==========================================================================
import turtle
import sys
import random
import turtle_interpreter as it
import shapes as shapes



def demolinestyles():
	square = shapes.Square()
	square.setWidth(1)
	square.setStyle('normal')
	square.draw(0, 200, 1, 90)
	square.setWidth(2)
	square.setStyle('normal')
	square.draw(200, 200, 1, 90)
	square.setWidth(3)
	square.setStyle('normal')
	square.draw(-200, 200, 1, 90)
	#=============================================
	square1 = shapes.Square()
	square1.setStyle('jitter')
	square1.setJitter(2)
	square1.draw(0, 50, 1, 90)
	square1.setStyle('jitter')
	square1.setJitter(3)
	square1.draw(200, 50, 1, 90)
	square1.setStyle('jitter')
	square1.setJitter(4)
	square1.draw(-200, 50, 1, 90)
	#=============================================
	square2 = shapes.Square()
	square2.setStyle('jitter3')
	square2.setJitter(2)
	square2.draw(0, -100, 1, 90)
	square2.setStyle('jitter3')
	square2.setJitter(3)
	square2.draw(200, -100, 1, 90)
	square2.setStyle('jitter3')
	square2.setJitter(4)
	square2.draw(-200, -100, 1, 90)
	#=============================================
	square3 = shapes.Square()
	square3.setStyle('slash')
	square3.setDotSize(1)
	square3.draw(0, -250, 1, 90)
	square3.setStyle('slash')
	square3.setDotSize(3)
	square3.draw(200, -250, 1, 90)
	square3.setStyle('slash')
	square3.setDotSize(5)
	square3.draw(-200, -250, 1, 90)
	
if __name__ == "__main__":
	demolinestyles()
	raw_input("Press enter to continue")