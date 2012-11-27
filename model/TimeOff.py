from sqlobject import *
from sqlobject.inheritance import *
from Request import *

class TimeOff(Request):
	day= IntCol()
	

