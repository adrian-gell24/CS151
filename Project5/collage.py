# Tony Karalekas
# Spring 2015
# CS 151 Project 5
# Collage.py file
# 
# Task 1 + 3
# --------------------------

# imports 

import graphics
import display
import sys
import filter

# -------------------------------


# Lab 5 Helper Functions
# The following functions are from Lab5 !!! 


# first step is to make a collage list
# clist = list of collage functions
clist = [	[ 'maine1.ppm', 0, 0, 'swapRedBlue', .80, False, None ],
			[ 'maine2.ppm', 150, 150, 'colorNegative', 0.60, False, None ],
			[ 'maine3.ppm', 0, 150, 'purpleHaze', 0.40, False, None],
			[ 'maine4.ppm', 150, 0, 'moreGreen', 0.20, False, None],
			[ 'me.ppm', 75, 75, 'original', 1.0 , True, None] 
		]
		

# readImage helper function

# reads in the files in the collage and stores pixmaps in the list
def readImages(clist):
	for item in clist:
		filename = 	item[0]
		src = graphics.Pixmap( filename )
		item[-1] = src
	


# getImageSize helper function 

# calculates how big the background Pixmap has to be to fit collage	
def getImageSize(clist):
	rows = 0
	cols = 0
	for item in clist:
		x0 = item[1]
		y0 = item[2]
		src = item[-1]
		dx = x0 + src.getWidth()
		if dx > cols:
			cols = dx
		dy = y0 + src.getHeight()
		if dy > rows:
			rows = dy
	return (cols, rows)

#====================================================================

# Project 5
# Task 1 + 3
# 
	
# this function builds the collage
# with all of its different parameter inputs	
def buildCollage( clist ):
	'''builds collage with input image lists
		with different filters, alpha values and locations'''
	(cols, rows) = getImageSize(clist)
	dst = graphics.Pixmap(cols, rows)
	for item in clist:
		filename = item[0]
		x0 = item[1]
		y0 = item[2]
		operator = item[3]
		alpha = item[4]
		noBkg = item[5]
		src = item[-1]
		if operator == 'swapRedBlue':
			filter.swapRedBlue(src)
		elif operator == 'colorNegative':
			filter.colorNegative(src)
		elif operator == 'purpleHaze':
			filter.purpleHaze(src)
		elif operator == 'moreGreen':
			filter.moreGreen(src)
		'''now considers boolean value of NoBkg
			and removes background if true'''
		if noBkg == True:
			filter.placePixmapNoBkg(dst, src, x0, y0, alpha)
		else:
			filter.placePixmap(dst, src, x0, y0, alpha)
		
	return dst

#-----------------------------------------------------

# this test function is from Lab5 work	
	
# test function for the read image function	
def test():
	'''useful test function for helper functions'''
	clist = [	[ 'maine1.ppm', 0, 0, 'swapRedBlue', .80, False, None ],
				[ 'maine3.ppm', 150, 150, 'colorNegative', 0.60, False, None ],
				[ 'maine3.ppm', 0, 150, 'purpleHaze', 0.40, False, None],
				[ 'maine4.ppm', 150, 0, 'moreGreen', 0.20, False, None],
				[ 'me.ppm', 75, 75, 'original', 1.0 , True, None] 
			]
	
	readImages(clist)
	
	#ask each image for its width and height
	for item in clist:
		print item[0]
		print item[-1].getWidth()
		print item[-1].getHeight()
		
	print getImageSize(clist)
	
test()
		
	