from sqlobject import *

#Could add more store info here, but don't see the use
# for the current application
class Store (SQLObject):
	name = StringCol()
	schedule = ForeignKey('Schedule')
	
