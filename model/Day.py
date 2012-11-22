from sqlobject import *

class Day(SQLObject):
	shifts = MultipleJoin('Shift')	
	store = ForeignKey('Store')
#If store hours = this then do all the shifts cover those hours
