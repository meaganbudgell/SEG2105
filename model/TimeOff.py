from sqlobject import *
from sqlobject.inheritance import *
from Request import *
from common import *

class TimeOff(Request):
	day= IntCol()
	
		
	def __get__dict(self):
		return to_dict(self)
