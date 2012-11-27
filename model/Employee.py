from sqlobject import *

import datetime

class Employee(SQLObject):
	name = StringCol()
	isManager = BoolCol()
	notifications = MultipleJoin('Notification', joinColumn="receiver_id")
	unavailableDays = MultipleJoin('UnavailableDay')
	stores = RelatedJoin('Store')
	requests = MultipleJoin('Request', joinColumn="sender_id_id")
	shifts = MultipleJoin('Shift')
	login = StringCol()
	
