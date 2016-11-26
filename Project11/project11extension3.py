# Tony Karalekas
# Spring 2015
# CS 151 Project 11
#
# project11 extension 3
#---------------------------------------------
#
#  Miller Library 3d Scene with 3d Lsystem from Extension 2
#
#==========================================================================
import turtle_interpreter as it
import shapes as s
import tree

# Extension 3
# MillerLibrary 3d Scene with my same shapes
# AND images from extension 1 and 2!

# Miller Library 
def Miller():
	'''rectangle for main body'''
	r = s.Rectangle()
	r.setWidth(3)
	r.setColor('SlateGray')
	r.draw(-150,-200, 1.75, 90)
	
	'''cubes for side of library'''
	c = s.Cube()
	c.setWidth(3)
	c.draw(-330, -200, 1.75, 90)
	c.draw(380, -200, 1.75, 90)
	
	'''trapezoid for middle body'''
	t = s.Trapezoid()
	t.setWidth(3)
	t.setColor('SlateGray')
	t.draw(-150, -25, 1.75, 90)
	
	'''rectangles for top and steps'''
	r.draw(-35, 128, 1, 90, zpos = 40)
	r.draw(40, 228, 0.5, 90, zpos = 60)
	r.draw(-110,-300, 1.5, 90)
	
	'''pyramids for the tops of side buildings'''
	p = s.Pyramid()
	p.setWidth(3)
	p.setColor('Gray')
	p.draw(-155, -25, 1.75, 90)
	p.draw(555, -25, 1.75, 90)
	
#==================================================================
	# EXTENSION WORK 
	# stars on sides of miller instead of diamonds
	'''decoration'''
	star = s.Star2()
	star.setWidth(2)
	star.setColor("LightBlue")
	star.draw(-223, 155, .5, 12, zpos = 110)
	star.draw(427, 155, .5, 12, zpos = 110)
	
	# EXTENSION WORK 
	# star on top of miller instead of cross
	'''decoration'''
	star = s.Star2()
	star.setColor("Blue")
	star.setWidth(3)
	star.draw(125, 340, 0.75, 90, zpos = 80)
	
	#Extension Work
	#TREEEEEES
	t1 = tree.Tree(filename= 'project11extension2a.txt')
	t1.setIterations(3)
	t1.setColor('OliveDrab')
	t1.draw(-130, -300, 2, 90, zpos = 300)
	t2 = tree.Tree(filename= 'project11extension2b.txt')
	t2.setIterations(3)
	t2.setColor('LawnGreen')
	t2.draw(330, -300, 2, 90, zpos = 300)	
	
	
if __name__ == "__main__":
	Miller()
	raw_input("Press enter to continue")