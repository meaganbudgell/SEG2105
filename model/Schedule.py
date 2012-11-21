from sqlobject import *

class Schedule(InheritableSQLObject):
	employees = MultipleJoin('Employee')
	shifts = MultipleJoin('Shift')
	stores = MultipleJoin('Store')
	
