from sqlobject import *

# Could add more store info here, but don't see the use
# for the current application
class Store (SQLObject):
	name = StringCol()
	employees = RelatedJoin('Employee')
	days = MultipleJoin('Day')
	
	def __init__(theName):
		name = theName
	
	def addEmployee(employee):
		employees.insert(employee)
		employee.stores.add(self)
		
	def removeEmployee(employee):
		employees.remove(employee)
		employee.stores.remove(self)