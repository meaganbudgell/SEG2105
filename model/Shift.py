from sqlobject import *

class Shift (SQLObject):

	startTime = DateTimeCol()
	endTime = DateTimeCol()
	schedule = ForeignKey('Schedule')
	
	def __init__(start, end, theSchedule)
		startTime = start
		endTime = end
		schedule = theSchedule