from sqlobject import *

class Schedule(InheritableSQLObject):
	#this employeeList may need to change, or we may decide
	#to get rid of PersonalSchedule completely... need to 
	#discuss this further.
	employeeList = MultipleJoin('Employee')
	shiftList = MultipleJoin('Shift')
	storeList = MultipleJoin('Store')
	
