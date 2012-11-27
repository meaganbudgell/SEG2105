from sqlobject import *
from sqlobject.inheritance import *
from Request import *
from common import *

class TimeOff(Request):
	day= IntCol()
	
		
	def _get_dict(self):
		return to_dict(self)
