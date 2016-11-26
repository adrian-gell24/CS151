# Tony Karalekas
# Spring 2015
# CS 151 Project 11
#
# shapes.py version 5
#---------------------------------------------
#
# 
#
#==========================================================================
import turtle_interpreter as it

class Shape:
	def __init__(self, distance = 100, angle = 90, color = (0,0,0), istring = '' ):
		self.distance = distance
		self.angle = angle
		self.color = color
		self.string = istring
		self.style = 'normal'
		self.jitterSigma = 2.0
		self.linewidth = 1.0
		
	def setColor(self, c):
		self.color = c
		
	def setDistance(self, d):
		self.distance = d
		
	def setAngle(self, a):
		self.angle = a
		
	def setString(self, s):
		self.string = s
		
	def setStyle(self, st):
		self.style = st
	
	def setJitter(self, js):
		self.jitterSigma = js
		
	def setWidth(self, w):
		self.linewidth = w
	
	def draw(self, xpos, ypos, scale = 1.0, orientation = 0, roll=0, pitch=0, zpos=0):
		terp = it.TurtleInterpreter()
		terp.place( xpos, ypos, orientation, pitch, roll, zpos )
		terp.color(self.color)
		terp.setJitter(self.jitterSigma)
		terp.setStyle(self.style)
		terp.width(self.linewidth)
		terp.drawString(self.string, self.distance*scale, self.angle)

class Square(Shape):
	def __init__(self, distance=100, color=(0, 0, 0) ):
		Shape.__init__(self, distance, 90, color, '{F-F-F-F-}')

class Triangle(Shape):
	def __init__(self, distance = 100, color = (0,0,0) ):
		Shape.__init__(self, distance, 120, color, '{F-F-F-}')
		
class Pentagon(Shape):
	def __init__(self, distance = 100, color = (0, 0, 0) ):
		Shape.__init__(self, distance, 72, color, '{F-F-F-F-F-}')

class Diamond(Shape):
	def __init__(self, distance = 100, color = (0,0,0) ):
		Shape.__init__(self, distance, 60, color, '{F--F-F--F-F--}')

class Star(Shape):
	def __init__(self, distance = 100, color = (0,0,0) ):
		Shape.__init__(self, distance, 51.5, color, 
						'{F---F++F---F++F---F++F---F++F---F++F---F++F---F++F---}')

class Cross(Shape):
	def __init__(self, distance = 50, color = (0,0,0) ):
		Shape.__init__(self, distance, 90, color, '{FF-F-FF+FF-F-FF+FF-F-FF+FF-F-FF}')
#====================================================================================

#Project 11 3-D Shapes for Task 1
# Cube, Rectangle, Trapezoid, and Diamond
		
class Cube(Shape):
	def __init__(self, distance=100, color=(0, 0, 0) ):
		Shape.__init__(self, distance, 90, color, '[F-F-F-F-F^F^F^F-F-F-F^F^F-F^^F^^^F]')
		
class Rectangle(Shape):
	def __init__(self, distance=100, color=(0, 0, 0) ):
		Shape.__init__(self, distance, 90, color, '-[FFF+F+FFF+F^F^F^F^^F+FFF+F--F&F&F&&F-FFF]')

class Trapezoid(Shape):
	def __init__(self, distance=100, color=(0, 0, 0) ):
		Shape.__init__(self, distance, 90, color, '[-FFF(120)+F(60)+FF(60)+F^F^F^F^^F^(60)+FF^F^^F^(60)+F^F^^F^(120)+FFF]')

class Diamond(Shape):
	def __init__(self, distance=100, color=(0, 0, 0) ):
		Shape.__init__(self, distance, 90, color, '[-F(155)+F(25)+F(155)+F&(.5)F&F&(0.5)F&&(0.5)F&(155)+F&(0.5)F&&(0.5)F&(25)+F&(0.5)F&&(0.5)F&(155)+F]')

#-------------------------------------------
### most of the code for this class was taken directly from test11-1.py 
class Pyramid(Shape):
	def __init__(self, distance=100, color=(0, 0, 0) ):
		Shape.__init__(self, distance, 90, color, '\&[F+F+F+[F(135)+(45)^F(90)&F](45)+(45)^F(90)&F]')

#----------------------------------------		
### RECIEVED This code from Julia Saul just to use in my scenes###
### Not as one of my shapes!! ###
'''Julia Saul helped me with this code'''

class Cross(Shape):
	def __init__(self, distance=100, color=(0, 0, 0) ):
		Shape.__init__(self, distance, 90, color, 'F-F+F+F-F+F+F-F+F+F-F+F^F^F[^F]+F[^F]-F[^F]+F[^F]+F[^F]-F[^F]+F[^F]+F[^F]-F[^F]+F[^F]+F[^F]-F[^F]')

#---------------------------------------------

# EXTENSION 1
# received help from Professor Maxwell
# 
class Star2(Shape):
	def __init__(self, distance=100, color=(0, 0, 0) ):
		Shape.__init__(self, distance, 51.5, color, '-[F(154.5)-F(103)+F(154.5)-F(103)+F(154.5)-F(103)+F(154.5)-F(103)+F(154.5)-F(103)+F(154.5)-F(103)+F(154.5)-F(103)+F[(12.25)+(135)^(2)F](154.5)-F(103)+F[(12.25)+(135)^(2)F](154.5)-F(103)+F[(12.25)+(135)^(2)F](154.5)-F(103)+F[(12.25)+(135)^(2)F](154.5)-F(103)+F[(12.25)+(135)^(2)F](154.5)-F(103)+F[(12.25)+(135)^(2)F](154.5)-F(103)+F[(12.25)+(135)^(2)F](154.5)-F(103)+F[(12.25)+(135)&(2)F](154.5)-F(103)+F[(12.25)+(135)&(2)F](154.5)-F(103)+F[(12.25)+(135)&(2)F](154.5)-F(103)+F[(12.25)+(135)&(2)F](154.5)-F(103)+F[(12.25)+(135)&(2)F](154.5)-F(103)+F[(12.25)+(135)&(2)F](154.5)-F(103)+F[(12.25)+(135)&(2)F](154.5)-F(103)+F')
																												
def test():
# 	c = Cube()
# 	c.setWidth(2)
# 	c.draw(-100, 150, 1, 90)
# 	trap = Trapezoid()
# 	trap.setWidth(2)
# 	trap.setStyle('dotted')
# 	trap.draw(200, 150, 1, 90)
# 	r = Rectangle()
# 	r.setWidth(2)
# 	r.setStyle('jitter3')
# 	r.draw(-200, -150, 1, 90)
# 	d = Diamond()
# 	d.setWidth(2)
# 	d.draw(300, -150, 1, 90)
	star = Star2()
	star.setWidth(3)
	star.setColor('Blue')
	star.draw(0,50,2,90)
	
if __name__ == "__main__":
	test()
	raw_input("Press enter to continue")
	