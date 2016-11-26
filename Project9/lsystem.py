# Tony Karalekas
# Spring 2015
# CS 151 Project 9
#
# lsystem.py version 3
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
	
	def replace(self, istring):
		tstring = ''
		for c in istring:
			if c in self.theListofRules.keys():
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

