# Tony Karalekas
# Spring 2015
# CS 151 Project 9
#
# shapes.py version 1
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
		
	def setColor(self, c):
		self.color = c
		
	def setDistance(self, d):
		self.distance = d
		
	def setAngle(self, a):
		self.angle = a
		
	def setString(self, s):
		self.string = s
	
	def draw(self, xpos, ypos, scale = 1.0, orientation = 0):
		terp = it.TurtleInterpreter()
		terp.place( xpos, ypos, orientation )
		terp.color(self.color)
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

def test():
	t = Triangle()
	s = Square()
	p = Pentagon()
	p.setColor('SteelBlue')
	d = Diamond()
	d.setColor('OliveDrab')
	st = Star()
	st.setColor('Gold')
	c = Cross()
	c.setColor('FireBrick')
	t.draw(0, 0, 1, 90)
	s.draw(0, 200, 1, 90)
	p.draw(-200, 0, 1, 90)
	c.draw(200, -100, 1, 90)
	d.draw(-200, -200, 1, 90)
	st.draw(300, 200, 1, 90)
	
if __name__ == "__main__":
	test()
	raw_input("Press enter to continue")