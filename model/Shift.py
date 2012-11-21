from sqlobject import *

class Shift (SQLObject):

	startTime = DateTimeCol()
	endTime = DateTimeCol()
	schedule = ForeignKey('Schedule')
	
	
