from sqlobject import *
from common import *

class Shift (SQLObject):

	startTime = DateTimeCol()
	endTime = DateTimeCol()
	employee = ForeignKey('Employee')
	store = ForeignKey('Store')
	isPreset = BoolCol(default=False)
	day = IntCol()

		
	def _get_dict(self):
		return toDict(self)
