from sqlobject import *

class Request (InheritableSQLObject):
	notification = SingleJoin('Notification')
	isApproved = BoolCol(Default=None)
	
