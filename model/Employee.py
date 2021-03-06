from sqlobject import *
from common import *
import datetime

class Employee(SQLObject):
	name = StringCol()
	isManager = BoolCol()
	notifications = MultipleJoin('Notification', joinColumn="receiver_id")
	unavailableDays = MultipleJoin('UnavailableDay')
	stores = RelatedJoin('Store')
	requests = MultipleJoin('Request', joinColumn="sender_id")
	shifts = MultipleJoin('Shift')
	login = StringCol()
	
		
	def _get_dict(self):
		return toDict(self)

	def checkLogin(self, inputLogin):
		if (self.login==inputLogin):
			return True
		else:
			return False
	

	
