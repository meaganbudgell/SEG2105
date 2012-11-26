from sqlobject import *

import datetime

class Employee(SQLObject):
	name = StringCol()
	isManager = BoolCol()
	notifications = MultipleJoin('Notification')
	unavailableDays = MultipleJoin('UnavailableDay')
	stores = RelatedJoin('Store')
	requests = MultipleJoin('Request')
	shifts = MultipleJoin('Shift')
	login = StringCol()
	
	def __init__(self, theName, manager, theLogin, store):
		name = theName
		isManager = manager
		login = theLogin
		
	def addUnavailableDay(self, theDay):
		someDay = UnavailableDay(theDay)
		unavailableDays.insert(someDay)
		
		# Did it work?
		try:
			test = unavailableDays.index(someDay)
			return True
		except IndexError:
			return False
	
	def removeUnavailableDay(self, theDay):
		someDay = UnavailableDay(theDay)
		unavailableDays.remove(someDay)
		
		# Did it work?
		try:
			test = unavailableDays.index(someDay)
			return False # The preceding line should fail
		except IndexError:
			return False