from sqlobject import *

class Notification(SQLObject):
	message = StringCol()
	timeStamp = DateTimeCol()
	request = SingleJoin('Request', default = None)
	receiver = ForeignKey('Employee')
