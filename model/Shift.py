from sqlobject import *

class Shift (SQLObject):

	startTime = DateTimeCol()
	endTime = DateTimeCol()
	employee = ForeignKey('Employee')
	day = ForeignKey('Day')
	isPreset = BoolCol(default=False)
	
	def __init__(start, end):
		startTime = start
		endTime = end
		
