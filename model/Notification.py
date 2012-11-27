from sqlobject import *
from common import *

class Notification(SQLObject):
	message = StringCol()
	timeStamp = DateTimeCol()
	request = SingleJoin('Request')
	receiver = ForeignKey('Employee')
	isSeen=BoolCol(default=False)

		
	def __get__dict(self):
		return to_dict(self)
	

