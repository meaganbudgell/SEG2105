from sqlobject import *
from common import *

class Notification(SQLObject):
	message = StringCol()
	timeStamp = DateTimeCol()
	request = SingleJoin('Request')
	receiver = ForeignKey('Employee')
	isSeen=BoolCol(default=False)

		
	def _get_dict(self):
		return toDict(self)
	
	def viewNotification(self):
		self.isSeen=True

