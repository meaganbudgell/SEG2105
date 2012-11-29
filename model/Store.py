from sqlobject import *
from common import *
import shelve

class Store (SQLObject):
	name = StringCol()
	employees = RelatedJoin('Employee')
	shifts = MultipleJoin('Shift')
	deadline=shelve.open("deadline.shelve")
	deadline["deadline"]=0
	openHour=StringCol()
	closeHour=StringCol()	
	
		
	def _get_dict(self):
		return toDict(self)
	def _get_openHour(self):
		return time.strptime(self.openHour)
	def _get_closeHour(self):
		return time.strptime(self.closeHour)
	
	def checkSchedule(self,shifts):
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

		
