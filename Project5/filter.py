# Tony Karalekas
# Spring 2015
# CS 151 Project 5
# Filter.py file
# 
# Task 2 + 3
# --------------------------

# imports 

import graphics
import display
import sys

#----------------------------------
# filters from Project 4
# create define multiple filters
# similar to original swapRedBlue() from lab
# but different varieties/more complex

# will use this same file with edits and additions
# throughout all of Lab 5 and Project 5


def swapRedBlue( pixm ):
	'''first filter from class -- simple'''
	for i in range( pixm.getHeight() ):
		for j in range( pixm.getWidth() ):
			(r, g, b) = pixm.getPixel( j, i )
			pixm.setPixel( j, i, (b,g,r) )
	
def colorNegative( pixm ):
	'''creates negative color filter'''
	for i in range( pixm.getHeight() ):
		for j in range( pixm.getWidth() ):
			(r, g, b) = pixm.getPixel( j, i )
			pixm.setPixel( j, i, (255-r, 255-g, 255-b) ) 

def purpleHaze( pixm ):
	'''creates purple haze filter'''
	for i in range( pixm.getHeight() ):
		for j in range( pixm.getWidth() ):
			(r, g, b) = pixm.getPixel( j, i )
			if b > r and b > g:
				pixm.setPixel( j, i, (0.75*r, 0.3*g, 0.7*b) )
			elif r > b and r >g:
				pixm.setPixel( j, i, (0.5*r, 0.5*g, 0.7*b) )
			elif g > b and g >r:
				pixm.setPixel( j, i, (0.65*r, 0.25*g, 0.75*b) )
				
def moreGreen( pixm ):
	'''creates extra green filter'''
	for i in range( pixm.getHeight() ):
		for j in range( pixm.getWidth() ):
			(r, g, b) = pixm.getPixel( j, i )
			pixm.setPixel( j, i, (0.3*r, g, 0.5*b) )
			
# =========================================================

# placePixmap function from Project4 with additions
# create placePixmap file with alpha
# takes five arguments
# alpha blending
# LAB 5 Notes

# NEW PlacePixmap function w/ alpha blending
# this places Pixmap image/file at given location(x,y) with alpha blending
def placePixmap( dst, src, x, y, alpha):
	''' used to position Pixmap in desired location
		now with alpha blending capabilities'''
	for i in range(src.getHeight()):
		for j in range(src.getWidth()):
			(r1, g1, b1) = src.getPixel( j, i )
			(r2, g2, b2) = dst.getPixel( j+x, i+y )
			rnew = r1*alpha + (1.0-alpha)*r2
			gnew = g1*alpha + (1.0-alpha)*g2
			bnew = b1*alpha + (1.0-alpha)*b2
			dst.setPixel( j+x, i+y, (rnew,gnew,bnew) )
	
# NEW function w/ alpha blending and background removal
# this places Pixmap image/file at given location(x,y) w/blending and w/o background
def placePixmapNoBkg(dst, src, x, y, alpha):
	''' used to position Pixmap in desired location
		now with alpha blending capabilities
		with green background removed'''	
	for i in range(src.getHeight()):
		for j in range(src.getWidth()):
			(r1, g1, b1) = src.getPixel( j, i )
			(r2, g2, b2) = dst.getPixel( j+x, i+y )
			rnew = r1*alpha + (1.0-alpha)*r2
			gnew = g1*alpha + (1.0-alpha)*g2
			bnew = b1*alpha + (1.0-alpha)*b2
			if g1<(1.5*r1) or g1<b1:
				dst.setPixel( j+x, i+y, (rnew, gnew, bnew))
			else:
			 	dst.setPixel( j+x, i+y, (r2, g2, b2))



#=========================================================
#--------------------------------------


# code from lab4
# used throughout project4
# test function for filters
# now being used in lab and project 5

	'''useful test function'''
def main(argv):
	''' reads in an image file and displays it in a window '''
	
	if len(argv) < 2:
		print "Usage: python show.py <filename>"
		exit()
		
	filename = argv[1]

	dst = graphics.Pixmap( filename )
	
	purpleHaze( dst )
	'''change this filter function to test out other filters'''
	
	win = display.displayPixmap( dst, filename )
	
	win.getMouse()
	
if __name__ == "__main__":
	main( sys.argv )


	