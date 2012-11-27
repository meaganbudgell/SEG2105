from sqlobject import *
from sqlobject.inheritance import *
from common import *

class Request (InheritableSQLObject):
	notification = ForeignKey('Notification')
	isApproved = BoolCol(default=None)
	sender = ForeignKey('Employee')

		
	def _get_dict(self):
		return to_dict(self)
