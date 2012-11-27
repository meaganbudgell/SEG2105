from sqlobject import *
from sqlobject.inheritance import *
from common import *

class Request (InheritableSQLObject):
	notification = ForeignKey('Notification')
	isApproved = BoolCol(default=None)
	sender = ForeignKey('Employee')

		
	def __get__dict(self):
		return to_dict(self)
