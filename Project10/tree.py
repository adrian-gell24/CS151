# Tony Karalekas
# Spring 2015
# CS 151 Project 9
#
# tree.py version 1
#---------------------------------------------
#imports

import lsystem as ls
import shapes as s
import turtle
import turtle_interpreter as it

#===========================================================

class Tree(s.Shape):

	def __init__(self, distance=5, angle=22.5, color=(0.5, 0.4, 0.3),
			iterations=3, filename=None):
		s.Shape.__init__(self, distance, angle, color, istring = '' )
		self.iterations = iterations
		self.lsys = ls.Lsystem(filename)

	def setIterations(self, iterations):
		self.iterations = iterations

	def read(self, filename):
		self.lsys.read(filename)

	def draw(self, xpos, ypos, scale = 1.0, orientation = 0):
		terp = it.TurtleInterpreter()
		terp.place( xpos, ypos, orientation )
		terp.color(self.color)
		self.string = self.lsys.buildString(self.iterations)
		terp.drawString(self.string, self.distance*scale, self.angle)
		
def test(filename):
	t1 = Tree(filename = filename)
	t1.setIterations(3)
	t1.setColor('OliveDrab')
	t2 = Tree(filename = filename)
	t2.setIterations(4)
	t2.setColor('Pink')
	t3 = Tree(filename = filename)
	t3.setIterations(5)
	t3.setColor('Sienna')
	t1.draw(-200, -300, 3, 90)
	t2.draw(0, -300, 3, 90)
	t3.draw(200, -300, 2, 90)
	
if __name__ == "__main__":
	test('systemJ.txt')
	raw_input("Press enter to continue")