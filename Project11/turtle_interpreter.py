# Tony Karalekas
# Spring 2015
# CS 151 Project 11
#
# turtle_interpreter.py version 5
#---------------------------------------------
#
# The purpose of this file is to convert a string
# into an image using simple turtle commands 
#
# Parameterized Strings and NPR 3D
#
#==========================================================================
import turtleTk3D
import sys
import random

# global variable turtle
turtle = None


class TurtleInterpreter:
	initialized = False

	def __init__(self, dx = 800, dy = 800):
		
		self.style = "normal"
		self.jitterSigma = 2.0
		self.dotSize = 5
		
		if TurtleInterpreter.initialized:
			return
			
		# new code
		global turtle
		turtle = turtleTk3D.Turtle3D(dx, dy)
		
		# old code	
		TurtleInterpreter.initialized = True
		turtle.setup()
		turtle.tracer(False)
		
	def drawString(self, dstring, distance, angle):
		stack = []
		cstack = []
		modstring = ''
		modval = None
		modgrab = False
		for c in dstring:
			if c == '(':
				modstring = ''
				modgrab = True
				continue
			elif c == ')':
				modval = float(modstring)
				modgrab = False
				continue
			elif modgrab:
				modstring += c
				continue
			elif c == 'F' or c ==  'f':
				if modval == None:
					self.forward(distance)
				else:
					self.forward(distance*modval)
			elif c == '-':
				if modval == None:
					turtle.right(angle)
				else:
					turtle.right(modval)
			elif c == '+':
				if modval == None:
					turtle.left(angle)
				else:
					turtle.left(modval)
			elif c == '!':
				if modval == None:
					w = turtle.width()
					if w > 1:
						turtle.width(w-1)
				else:
					turtle.width(modval)
			elif c == '[':
				stack.append(turtle.position())
				stack.append(turtle.heading())
				stack.append(turtle.width())
			elif c == ']':
				turtle.up()
				turtle.width(stack.pop())
				turtle.setheading(stack.pop())
				turtle.goto(stack.pop())
				turtle.down()
			elif c == 'L':
				#draws a leaf
				#begin and end fil calls work better in this section of code
				turtle.begin_fill()
				turtle.circle(5)
				turtle.end_fill()
			elif c == 'Q':
				#created for task3
				#draws a flower
				pos = turtle.position()
				heading = turtle.heading()
				turtle.begin_fill()
				turtle.right(90)
				turtle.forward(5)
				turtle.left(120)
				turtle.forward(10)
				turtle.left(120)
				turtle.forward(10)
				turtle.left(120)
				turtle.forward(10)
				turtle.end_fill()
				turtle.up()
				turtle.goto(pos)
				turtle.setheading(heading)
				turtle.down()
			elif c == 'P':
				#draws a petal
				#CREATED FOR EXTENSION1
				turtle.begin_fill()
				for i in range(12):
					turtle.forward(5)
					turtle.right(108)
					turtle.forward(5)
					turtle.left(144)
				turtle.end_fill()
			elif c == '<':
				color = turtle.color()
				cstack.append(color)
			elif c == '>':
				turtle.color(cstack.pop())
			elif c == 'g':
				#makes the leaf color medium orchid
				turtle.color("Medium Orchid")
			elif c == 'y':
				#makes the leaf color turquoise
				turtle.color("Turquoise")
			elif c == 'r':
				#makes the leaf color salmon
				turtle.color("Salmon")
			elif c == 'b':
				#CREATED FOR EXTENSION1
				#makes the leaf color salmon
				turtle.color("Plum")
			elif c == 'o':
				#CREATED FOR EXTENSION1
				#makes the leaf color salmon
				turtle.color("Khaki")
			elif c == '{':
				turtle.fill(True)
			elif c == '}':
				turtle.fill(False)
			elif c == '&':
				if modval == None:
					turtle.pitch(angle)
				else:
					turtle.pitch(modval)
			elif c == '^':
				if modval == None:
					turtle.pitch(-angle)
				else:
					turtle.pitch(-modval)
			elif c == '/':
				if modval == None:
					turtle.roll(-angle)
				else:
					turtle.roll(-modval)
			elif c == '\\':
				if modval == None:
					turtle.roll(angle)
				else:
					turtle.roll(modval)
		
			modval = None	
			
		turtle.update()
	
	def color(self, c):
		turtle.color = c
		
	def hold(self):
		""" holds the screen open until the user clicks or types 'q' """
		# start the main loop until an event happens, then exit
		turtle.mainloop()
		
		
	def place(self, xpos, ypos, angle=None, pitch=0, roll=0, zpos=0): 
		turtle.up()
		turtle.goto( xpos, ypos, zpos )
		if angle != None:
			turtle.setheading(angle)
			self.orient(angle, roll, pitch)
		turtle.down()

	def orient(self, angle, roll=0, pitch= 0): 
		turtle.setheading(0)
		turtle.roll(roll)
		turtle.pitch(pitch)
		turtle.yaw(angle)

	def goto(self, xpos, ypos, zpos=0): 
		turtle.up()
		turtle.goto( xpos, ypos, zpos )
		turtle.down()
		
	def roll(self, roll):
		turtle.roll(roll)
	
	def pitch(self, pitch):
		turtle.pitch(pitch)
	
	def yaw(self, yaw):
		turtle.yaw(yaw)
		
	def color(self, c): 
		turtle.color(c)
	
	def width(self, w): 
		turtle.width(w)
		
	def setStyle(self, s):
		self.style = s
	
	def setJitter(self, j):
		self.jitterSigma = j
	
	def setDotSize(self, ds):
		self.dotSize = ds
		
	def forward(self, distance):
		if self.style == 'normal':
			turtle.forward(distance)
		
		elif self.style == 'jitter':
			(x0, y0, z0) = turtle.position()
			turtle.up()
			turtle.forward(distance)
			(xf, yf, zf) = turtle.position()
			curwidth = turtle.width()
			
			jx = random.gauss(0, self.jitterSigma)
			jy = random.gauss(0, self.jitterSigma)
			jz = random.gauss(0, self.jitterSigma)
			kx = random.gauss(0, self.jitterSigma)
			ky = random.gauss(0, self.jitterSigma)
			kz = random.gauss(0, self.jitterSigma)
			
			curwidth += random.randint(0,2)
			turtle.goto(x0+jx, y0+jy, z0+jz)
			turtle.down()
			turtle.goto(xf+kx, yf+ky, zf+kz)
			turtle.up()
			turtle.goto(xf,yf, zf)
			curwidth = turtle.width()
			turtle.down()
					
		elif self.style == 'jitter3':
			(x0, y0, z0) = turtle.position()
			turtle.up()
			turtle.forward(distance)
			(xf, yf, zf) = turtle.position()
			curwidth = turtle.width()
			
			jx = random.gauss(0, self.jitterSigma)
			jy = random.gauss(0, self.jitterSigma)
			jz = random.gauss(0, self.jitterSigma)
			kx = random.gauss(0, self.jitterSigma)
			ky = random.gauss(0, self.jitterSigma) 
			kz = random.gauss(0, self.jitterSigma)
			lx = random.gauss(0, self.jitterSigma)
			ly = random.gauss(0, self.jitterSigma)
			lz = random.gauss(0, self.jitterSigma)
			mx = random.gauss(0, self.jitterSigma)
			my = random.gauss(0, self.jitterSigma) 
			mz = random.gauss(0, self.jitterSigma)
			nx = random.gauss(0, self.jitterSigma)
			ny = random.gauss(0, self.jitterSigma)
			nz = random.gauss(0, self.jitterSigma)
			ox = random.gauss(0, self.jitterSigma)
			oy = random.gauss(0, self.jitterSigma)
			oz = random.gauss(0, self.jitterSigma)
			 
			curwidth += random.randint(0,2)
			turtle.goto(x0+jx, y0+jy, z0+jz)
			turtle.down()
			turtle.goto(xf+kx, yf+ky, zf+kz)
			turtle.up()
			turtle.goto(x0+lx, y0+ly, z0+lz)
			turtle.down()
			turtle.goto(xf+mx, yf+my, zf+mz)
			turtle.up()
			turtle.goto(x0+nx, y0+ny, z0+nz)
			turtle.down()
			turtle.goto(xf+ox, yf+oy, zf+oz)
			curwidth = turtle.width()
			turtle.down()
		
		elif self.style == 'dotted':
			num_dots = int(distance/(self.dotSize*4))
			(x0, y0, z0) = turtle.position()
			turtle.up()
			turtle.forward(distance)
			(xf, yf, zf) = turtle.position()
			curwidth = turtle.width()
			turtle.goto(x0, y0, z0)
			for i in range(num_dots):
				turtle.down()
				turtle.circle(self.dotSize)
				turtle.up()
				turtle.forward(self.dotSize*4)
			turtle.goto(xf, yf, zf)
		
		# EXTENSION 1
		elif self.style == 'slash':
			num_slash = int(distance/10)
			(x0, y0) = turtle.position()
			turtle.up()
			turtle.forward(distance)
			(xf, yf) = turtle.position()
			curwidth = turtle.width()
			turtle.goto(x0, y0)
			for i in range(num_slash):
				turtle.left(45)
				turtle.forward(distance/25)
				turtle.up()
				turtle.right(180)
				turtle.down()
				turtle.forward(distance/25)
				turtle.up()
				turtle.right(225)
				turtle.forward(num_slash)
				turtle.down()
	
	
