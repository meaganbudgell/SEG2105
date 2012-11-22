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
	
	def __init__(theName, manager):
		name = theName
		isManager = manager