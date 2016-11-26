# Tony Karalekas
# Spring 2015
# CS 151 Project 10
#
# lsystem.py version 4
#---------------------------------------------
#
#
#
#=========================================================================
#
import sys 
import random
import turtle


class Lsystem:
	def __init__( self, filename = None ):
		'''Creates the fields for a new Lsystem object'''
		self.theBaseStringForTheLsystem = ''
		self.theListofRules = {}
		if filename != None:
			self.read(filename)
			
	def setBase(self,base):
		'''Sets the base string to the new value'''
		self.theBaseStringForTheLsystem = base
		
	def getBase(self):
		return self.theBaseStringForTheLsystem
		
	def addRule(self, newrule):
		self.theListofRules[newrule[0]] = newrule[1:]
		
	def getRule(self, index):
		return self.theListofRules.get(index, index)
	
	def read( self, filename ):
		fp = open(filename)
		lines = fp.readlines()
		fp.close()
		for line in lines:
			words = line.split()
			if words[0] == 'base':
				self.setBase(words[1]) 
			elif words[0] =='rule':
				self.addRule(words[1:])
	
	
	def substitute(self, sequence, value ):
		""" given: a sequence of parameterized symbols using expressions
			of the variable x and a value for x
			substitute the value for x and evaluate the expressions
		"""

		expr = ''
		exprgrab = False

		outsequence = ''

		for c in sequence:

			# parameter expression starts
			if c == '(':
				# set the state variable to True (grabbing the expression)
				exprgrab = True
				expr = ''
				continue

			# parameter expression ends
			elif c == ')':
				exprgrab = False
				# create a function out of the expression
				lambdafunc = eval( 'lambda x: ' + expr )
				# execute the function and put the result in a (string)
				newpar = '(' + str( lambdafunc( value ) ) + ')'
				outsequence += newpar

			# grabbing an expression
			elif exprgrab:
				expr += c

			# not grabbing an expression and not a parenthesis
			else:
				outsequence += c 

		return outsequence

	def insertmod(self, sequence, modstring, symbol):
		""" given: a sequence, a parameter string, a symbol 
			inserts the parameter, with parentheses, 
			before each
			instance of the symbol in the sequence
		"""
		tstring = ''
		for c in sequence:
			if c == symbol:
				# add the parameter string in parentheses
				tstring += '(' + modstring + ')'
			tstring += c
		return tstring
	
	
	def replace(self, istring):
		""" Replace all characters in the istring with strings from the
			right-hand side of the appropriate rule. This version handles
			parameterized rules.
		"""
		tstring = ''
		parstring = ''
		parval = None
		pargrab = False

		for c in istring:
			if c == '(':
				# put us into number-parsing-mode
				pargrab = True
				parstring = ''
				continue
			# elif the character is )
			elif c == ')':
				# put us out of number-parsing-mode
				pargrab = False
				parval = float(parstring)
				continue
			# elif we are in number-parsing-mode
			elif pargrab:
				# add this character to the number string
				parstring += c
				continue

			if parval != None:
				key = '(x)' + c
				if key in self.theListofRules:
					replacement = random.choice(self.theListofRules[key])
					tstring += self.substitute( replacement, parval )
				else:
					if c in self.theListofRules:
						replacement = random.choice(self.theListofRules[c])
						tstring += self.insertmod( replacement, parstring, c )
					else:
						tstring += '(' + parstring + ')' + c
				parval = None
			else:
				if c in self.theListofRules:
					tstring += random.choice(self.theListofRules[c])
				else:
					tstring += c

		return tstring
			

	def buildString(self, iterations):
		nstring = self.theBaseStringForTheLsystem
		for i in range(iterations):
			nstring = self.replace(nstring)
		return nstring
  
def main(argv):

  if len(argv) < 4:
	print 'Usage: lsystem.py <filename> <iterations> <output file>'
	exit()

  filename = argv[1]
  iterations = int(argv[2])
  outfile = argv[3]

  lsys = Lsystem()

  lsys.read( filename )

  print lsys
  print lsys.getBase()
  print lsys.getRule(0)

  lstr = lsys.buildString( iterations )

  fp = file( outfile, 'w' )
  fp.write(lstr)
  fp.close()

  return


if __name__ == "__main__":
  main(sys.argv)

