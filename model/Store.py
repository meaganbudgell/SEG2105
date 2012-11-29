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

	
	def checkSchedule(self,shifts):
		for i, val in enumerate(shifts):
			try:
				if (shifts[i].endTime<= shifts[i+1].startTime):
					pass
				else:
					return False	
			except IndexError, e:
				if (shifts[i].endTime==self.closeHour):
					return True

		if(shifts[0].startTime==self.openHour):		
			return True
		else:
			return False

		
