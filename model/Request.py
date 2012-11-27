from sqlobject import *
from sqlobject.inheritance import *

class Request (InheritableSQLObject):
	notification = ForeignKey('Notification')
	isApproved = BoolCol(default=None)
	sender = ForeignKey('Employee')

