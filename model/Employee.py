from sqlobject import *

class Employee(SQLObject):
	name = StringCol()
	isManager = BoolCol()
	notifications = MultipleJoin('Notification')
	unavailableDays = MultipleJoin('UnavailableDay')
	masterSchedule = ForeignKey('Schedule')
	requests = MutlipleJoin('Request')
	login = StringCol()

# Due to how SQLObject works, a class is required to create a table
# so an attribute can contain multiple values. In this case, a list of 
# integers corresponding to days of the year.
class UnavailableDay(SQLObject):
	dayNumber = IntCol()
	employee = ForeignKey ('Employee')
