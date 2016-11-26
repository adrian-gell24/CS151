# Tony Karalekas
# Spring 2015
# CS 151 Project 11
#
# 3dscene.py version1
#---------------------------------------------
#
# 
#
#==========================================================================
import turtle_interpreter as it
import shapes as s


#def ground():

# base of the castle	
def base():
	'''this function draws the trapezoid base of the castle'''
	trap = s.Trapezoid()
	trap.setWidth(8)
	trap.setColor('SlateGray')
	trap.draw(-345, -245, 2.25, 90)
	cross = s.Cross()
	cross.setWidth(2)
	cross.setColor('OliveDrab')
	cross.draw(100, -150, 0.25, 90, zpos = 90)
	cross.setColor('OliveDrab')
	cross.draw(-100, -150, 0.25, 90, zpos = 90)
	
#------------------------------
# HOUSE 1, 2, 3
def house1():
	'''this function draws the cube house1 of the castle'''
	c = s.Cube()
	c.setWidth(8)
	c.setColor('SlateGray')
	c.draw(-100, -50, 2, 90)
	p = s.Pyramid()
	p.setColor('RoyalBlue')
	p.setWidth(6)
	p.draw(100, 150, 2, 90)
	d = s.Diamond()
	d.setWidth(2)
	d.setColor('Red')
	d.draw(-210, 340, 0.5, 12, zpos = 115)
	
def house2():
	'''this function draws the cube house2 of the castle'''
	c = s.Cube()
	c.setWidth(8)
	c.setColor('SlateGray')
	c.draw(-300, -50, 2, 90)
	p = s.Pyramid()
	p.setColor('Goldenrod')
	p.setWidth(6)
	p.draw(-100, 150, 2, 90)
	cross = s.Cross()
	cross.setWidth(2)
	cross.setColor('Purple')
	cross.draw(12, 292, 0.25, 90, zpos = 90)
	
def house3():
	'''this function draws the cube house3 of the castle'''
	c = s.Cube()
	c.setWidth(8)
	c.setColor('SlateGray')
	c.draw(100, -50, 2, 90)
	p = s.Pyramid()
	p.setWidth(6)
	p.setColor('Goldenrod')
	p.draw(300, 150, 2, 90)
	d = s.Diamond()
	d.setWidth(2)
	d.setColor('Red')
	d.draw(190, 340, 0.5, 12, zpos = 115)

#-------------------------------
	
def Kings():
	'''kings in the main part of the castle'''
	d = s.Diamond()
	d.setWidth(6)
	d.setColor('Goldenrod')
	d.draw(-25, 50, 1, 12, zpos = 100)
	
	d = s.Diamond()
	d.setWidth(4)
	d.setColor('RoyalBlue')
	d.draw(175, 50, 1, 12, zpos = 100)
	
	d = s.Diamond()
	d.setWidth(4)
	d.setColor('RoyalBlue')
	d.draw(-225, 50, 1, 12, zpos = 100)

def soliders():
	'''soldiers in the keep of the castle in formation'''
	d = s.Diamond()
	d.setWidth(2)
	d.setColor('Red')
	d.draw(-250, -220, 0.25, 12, zpos = 25)
	d.draw(-250, -220, 0.25, 12, zpos = 50)
	d.draw(-250, -220, 0.25, 12, zpos = 75)
	d.draw(-250, -220, 0.25, 12, zpos = 100)
	d.draw(-250, -220, 0.25, 12, zpos = 125)
	d.draw(-250, -220, 0.25, 12, zpos = 150)
	d.draw(-250, -220, 0.25, 12, zpos = 175)
	d.draw(-250, -220, 0.25, 12, zpos = 200)
	
	d.setColor('Purple')
	d.draw(-200, -220, 0.25, 12, zpos = 25)
	d.draw(-200, -220, 0.25, 12, zpos = 50)
	d.draw(-200, -220, 0.25, 12, zpos = 75)
	d.draw(-200, -220, 0.25, 12, zpos = 100)
	d.draw(-200, -220, 0.25, 12, zpos = 125)
	d.draw(-200, -220, 0.25, 12, zpos = 150)
	d.draw(-200, -220, 0.25, 12, zpos = 175)
	d.draw(-200, -220, 0.25, 12, zpos = 200)
	
	d.setColor('Red')
	d.draw(-150, -220, 0.25, 12, zpos = 25)
	d.draw(-150, -220, 0.25, 12, zpos = 50)
	d.draw(-150, -220, 0.25, 12, zpos = 75)
	d.draw(-150, -220, 0.25, 12, zpos = 100)
	d.draw(-150, -220, 0.25, 12, zpos = 125)
	d.draw(-150, -220, 0.25, 12, zpos = 150)
	d.draw(-150, -220, 0.25, 12, zpos = 175)
	d.draw(-150, -220, 0.25, 12, zpos = 200)
	
	d.setColor('Purple')
	d.draw(-100, -220, 0.25, 12, zpos = 25)
	d.draw(-100, -220, 0.25, 12, zpos = 50)
	d.draw(-100, -220, 0.25, 12, zpos = 75)
	d.draw(-100, -220, 0.25, 12, zpos = 100)
	d.draw(-100, -220, 0.25, 12, zpos = 125)
	d.draw(-100, -220, 0.25, 12, zpos = 150)
	d.draw(-100, -220, 0.25, 12, zpos = 175)
	d.draw(-100, -220, 0.25, 12, zpos = 200)
	
	d.setColor('Red')
	d.draw(-50, -220, 0.25, 12, zpos = 25)
	d.draw(-50, -220, 0.25, 12, zpos = 50)
	d.draw(-50, -220, 0.25, 12, zpos = 75)
	d.draw(-50, -220, 0.25, 12, zpos = 100)
	d.draw(-50, -220, 0.25, 12, zpos = 125)
	d.draw(-50, -220, 0.25, 12, zpos = 150)
	d.draw(-50, -220, 0.25, 12, zpos = 175)
	d.draw(-50, -220, 0.25, 12, zpos = 200)
	
	d.setColor('Purple')
	d.draw(0, -220, 0.25, 12, zpos = 25)
	d.draw(0, -220, 0.25, 12, zpos = 50)
	d.draw(0, -220, 0.25, 12, zpos = 75)
	d.draw(0, -220, 0.25, 12, zpos = 100)
	d.draw(0, -220, 0.25, 12, zpos = 125)
	d.draw(0, -220, 0.25, 12, zpos = 150)
	d.draw(0, -220, 0.25, 12, zpos = 175)
	d.draw(0, -220, 0.25, 12, zpos = 200)
	
	d.setColor('Red')
	d.draw(50, -220, 0.25, 12, zpos = 25)
	d.draw(50, -220, 0.25, 12, zpos = 50)
	d.draw(50, -220, 0.25, 12, zpos = 75)
	d.draw(50, -220, 0.25, 12, zpos = 100)
	d.draw(50, -220, 0.25, 12, zpos = 125)
	d.draw(50, -220, 0.25, 12, zpos = 150)
	d.draw(50, -220, 0.25, 12, zpos = 175)
	d.draw(50, -220, 0.25, 12, zpos = 200)
	
	d.setColor('Purple')
	d.draw(100, -220, 0.25, 12, zpos = 25)
	d.draw(100, -220, 0.25, 12, zpos = 50)
	d.draw(100, -220, 0.25, 12, zpos = 75)
	d.draw(100, -220, 0.25, 12, zpos = 100)
	d.draw(100, -220, 0.25, 12, zpos = 125)
	d.draw(100, -220, 0.25, 12, zpos = 150)
	d.draw(100, -220, 0.25, 12, zpos = 175)
	d.draw(100, -220, 0.25, 12, zpos = 200)
	
	d.setColor('Red')
	d.draw(150, -220, 0.25, 12, zpos = 25)
	d.draw(150, -220, 0.25, 12, zpos = 50)
	d.draw(150, -220, 0.25, 12, zpos = 75)
	d.draw(150, -220, 0.25, 12, zpos = 100)
	d.draw(150, -220, 0.25, 12, zpos = 125)
	d.draw(150, -220, 0.25, 12, zpos = 150)
	d.draw(150, -220, 0.25, 12, zpos = 175)
	d.draw(150, -220, 0.25, 12, zpos = 200)
	
	d.setColor('Purple')
	d.draw(200, -220, 0.25, 12, zpos = 25)
	d.draw(200, -220, 0.25, 12, zpos = 50)
	d.draw(200, -220, 0.25, 12, zpos = 75)
	d.draw(200, -220, 0.25, 12, zpos = 100)
	d.draw(200, -220, 0.25, 12, zpos = 125)
	d.draw(200, -220, 0.25, 12, zpos = 150)
	d.draw(200, -220, 0.25, 12, zpos = 175)
	d.draw(200, -220, 0.25, 12, zpos = 200)

	d.setColor('Red')
	d.draw(250, -220, 0.25, 12, zpos = 25)
	d.draw(250, -220, 0.25, 12, zpos = 50)
	d.draw(250, -220, 0.25, 12, zpos = 75)
	d.draw(250, -220, 0.25, 12, zpos = 100)
	d.draw(250, -220, 0.25, 12, zpos = 125)
	d.draw(250, -220, 0.25, 12, zpos = 150)
	d.draw(250, -220, 0.25, 12, zpos = 175)
	d.draw(250, -220, 0.25, 12, zpos = 200)
	
#-----------------------------------------------	

if __name__ == "__main__":
	house1()
	house2()
	house3()
	base()
	soliders()
	Kings()
	raw_input("Press enter to continue")