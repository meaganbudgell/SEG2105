from sqlobject import *

class Notification(SQLObject):
	message = StringCol()
	timeStamp = DateTimeCol()
	request = SingleJoin('Request')
	receiver = ForeignKey('Employee')
	
	def __init__(self, theMessage, theRequest):
		message = theMessage
		request = theRequest