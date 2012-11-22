from sqlobject import *
from sqlobject.inheritance import *
from Request import *

class TimeOff(Request):
	dayNumber = IntCol()
	
	def __init__(day):
		dayNumber = day.timetuple().tm_yday