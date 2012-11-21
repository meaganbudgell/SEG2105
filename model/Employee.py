from sqlobject import *

class Employee(SQLObject):
	name = StringCol()
	isManager = BoolCol()
	notificationList = MultipleJoin('Notification')
	personalSchedule = ForeignKey('PersonalSchedule')
	masterSchedule = ForeignKey('Schedule')
	requestList = MutlipleJoin('Request')
	login = StringCol()
