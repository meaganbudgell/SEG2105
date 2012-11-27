from sqlobject import *
from common import *

class Shift (SQLObject):

	startTime = DateTimeCol()
	endTime = DateTimeCol()
	employee = ForeignKey('Employee')
	day = ForeignKey('Day')
	isPreset = BoolCol(default=False)

		
	def _get_dict(self):
		return to_dict(self)
