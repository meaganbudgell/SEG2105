from sqlobject import *
from common import *

# Could add more store info here, but don't see the use
# for the current application
class Store (SQLObject):
	name = StringCol()
	employees = RelatedJoin('Employee')
	days = RelatedJoin('Day')
	
		
	def __get__dict(self):
		return to_dict(self)
