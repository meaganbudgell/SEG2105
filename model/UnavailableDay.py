from sqlobject import *


# Due to how SQLObject works, a class is required to create a table
# so an attribute can contain multiple values. In this case, a list of 
# integers corresponding to days of the year.
class UnavailableDay(SQLObject):
	dayNumber = IntCol()
	employee = ForeignKey ('Employee')

	def __init__(self, day):
		# This converts the datetime object into the "day number"
		dayNumber = day.timetuple().tm_yday
