from sqlobject import *

class Schedule(SQLObject):
	employees = MultipleJoin('Employee')
	shifts = MultipleJoin('Shift')
	stores = MultipleJoin('Store')
	
