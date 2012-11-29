from sqlobject import *
from common import *

class Shift (SQLObject):

	startTime = DateTimeCol()
	endTime = DateTimeCol()
	employee = ForeignKey('Employee')
	store = ForeignKey('Store')
	isPreset = BoolCol(default=False)
	day = IntCol()

		
	def _get_dict(self):
		return toDict(self)

	def addEmployee(self, employee):
		self.employee=employee.id

	def removeEmployee(self, employee):
		self.employee=None
	
	def addDay(self day_id):
		self.day=day_id

	#This means the Shift itself is deleted.
	def removeDay(self):
		self.destroySelf()
	
