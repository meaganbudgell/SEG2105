from sqlobject import *
from common import *


class UnavailableDay(SQLObject):
	dayNumber = IntCol()
	employee = ForeignKey ('Employee')

		# This converts the datetime object into the "day number"
		#dayNumber = day.timetuple().tm_yday

		
	def _get_dict(self):
		return to_dict(self)
