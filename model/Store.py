from sqlobject import *
from common import *
import shelve

# Could add more store info here, but don't see the use
# for the current application
class Store (SQLObject):
	name = StringCol()
	employees = RelatedJoin('Employee')
	shifts = MultipleJoin('Shift')
	deadline=shelve.open("deadline.shelve")
	deadline["deadline"]=0	
	
		
	def _get_dict(self):
		return toDict(self)
