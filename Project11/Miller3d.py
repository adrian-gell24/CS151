# Tony Karalekas
# Spring 2015
# CS 151 Project 11
#
# Miller3d.py version1
#---------------------------------------------
#
# TASK 3 and (possibly extension material) 
#
#==========================================================================
import turtle_interpreter as it
import shapes as s

# Task 3
# New Scene with my same shapes

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
	
	'''decoration'''
	d = s.Diamond()
	d.setWidth(2)
	d.setColor("LightBlue")
	d.draw(-263, 195, 1, 12, zpos = 110)
	d.draw(447, 195, 1, 12, zpos = 110)
	
	'''decoration'''
	cross = s.Cross()
	cross.setColor("Blue")
	cross.setWidth(4)
	cross.draw(130, 278, 0.35, 90, zpos = 70)
	
	
	
if __name__ == "__main__":
	Miller()
	raw_input("Press enter to continue")