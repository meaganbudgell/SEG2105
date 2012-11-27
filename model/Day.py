from sqlobject import *
from common import *

class Day(SQLObject):
	shifts = MultipleJoin('Shift')	
	store = RelatedJoin('Store')
	
	def __get__dict(self):
		return to_dict(self)

		
	def addShift(self, theShift):
		shifts.insert(theShift)
		
		# Did it actually work?
		try:
			test = shifts.index(theShift)
			return True
		except IndexError:
			return False
		
	def removeShift(self, theShift):
		shifts.remove(theShift)
		
		# Did it actually work?
		try:
			test = shifts.index(theShift)
			return False # The preceding line should fail
		except IndexError:
			return True
