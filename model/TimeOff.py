from sqlobject import *

class TimeOff(Request)
	shifts = MultipleJoin ('Shift')
	
