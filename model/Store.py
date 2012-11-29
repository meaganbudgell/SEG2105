from sqlobject import *
from common import *
import shelve
from datetime import *

class Store (SQLObject):
	name = StringCol()
	employees = RelatedJoin('Employee')
	shifts = MultipleJoin('Shift')
	deadline=shelve.open("deadline.shelve")
	deadline["deadline"]=0
	openHour=DateTimeCol()
	closeHour=DateTimeCol()	
	
		
	def _get_dict(self):
		return toDict(self)

	#evaluates the list of shifts from a given day.
	def checkSchedule(self,s):
		for i, val in enumerate(s):
			try:
				if (s[i].endTime<= s[i+1].startTime):
					pass
				else:
					return False	
			except IndexError, e:
				if (s[i].endTime==self.closeHour):
					return True

		if(s[0].startTime==self.openHour):		
			return True
		else:
			return False

		
