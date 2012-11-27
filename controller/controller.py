from model import *

#Converts objects into dictionaries so Bottle can output JSON !
def toDict(obj):
		# each type of column
		foreigns = obj.sqlmeta._plainForeignGetters.keys()
		joins = obj.sqlmeta.joinDefinitions

		# all of the basic stuff is built-in 
		d = obj.sqlmeta.asDict()

		# convert all datetimes/dates/times to something JSON can use
		for k in d:
		       if isinstance(d[k], datetime.datetime) or isinstance(d[k], datetime.date) or isinstance(d[k], datetime.time):
			       d[k] = d[k].isoformat()

		# function given class and list of objects of that class, returns object dict for that reference
		# an object dict is a dictionary with 2 keys.  name is the name of the class that the objects contained are instances of
		# items is the list of IDs referenced.
		def f(klass, objs):
		       return dict(name=klass,
				   items=[x.id for x in objs])

		# convert all foreign keys to one-element object dicts
		for key in foreigns:
		       d.update({key:f(getattr(obj, key)._class_._name_, [getattr(obj, key)])})

		# convert all joins to object dicts
		for key in joins:
		       d.update({key.name:f(key.kw['otherClass'], getattr(obj, key.name))})
       
       		return d

def checkLogin(name, login):
	pass

def getMonthDetails(date):
	pass

def loadSchedule(employee_id):
	pass

def checkSchedule(date):
	pass

def loadNotifications(name):
	pass

def loadRequests(name):
	pass

def answerRequest(isApproved):
	pass

def addShiftBlock(startTime, endTime):
	pass

def addEmployee(name, isManager, loginPassword, store_id):
	# Creates a new employee
	e = Employee()
	e.name = name
	e.isManager = isManager
	e.login = login
	e.stores.insert(store_id)

def loadEmployeeList(storeName):
	pass

def loadStoreList():
	pass

def loadTemplateShifts():
	pass

def removeShiftBlock(shift_id):
	pass

def addEmployeeToShift(employee, shift_id):
	# Adds the given employee to the given shift
	shift_id.employee = employee

def checkAvailableEmployees(shift_id):
	pass

def addShiftToDay(shift_id, day_id):
	# Adds the given shift to the given day
	day_id.addShift(shift_id)

def removeShiftFromDay(shift_id, day_id):
	# Removes the given shift from the given day
	day_id.removeShift(shift_id)

def loadDay(day_id):
	pass

def addUnavailableDay(day_id):
	pass

def removeUnavailableDay(day_id):
	pass

def getScheduleDeadline():
	pass

def setScheduleDeadline(date):
	pass

def addTimeOffRequest(employee_id, date):
	pass

def viewNotification(isSeen):
	pass
