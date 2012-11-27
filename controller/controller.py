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

def checkLogin(inputName, inputLogin):
	# If name is not in db, catches error and returns false.
	try:
		#Grabs Employee with the same name. Compares that login with the input one. True or False Accordingly.
		n = Employee.select(Employee.q.name == inputName)[0]
		if (n.login==inputLogin):
			return True
		else:
			return False
	except IndexError, e:
		return False

def getMonthDetails(date):
	pass

def loadSchedule(employee_id):
	pass

def checkSchedule(date):
	pass

def loadNotifications(name):
	# Return all of the notifications
	result = list()

def loadRequests(name):
	# Return all of the requests
	result = list()
	for r in Request.select():
		result.insert(Request.select(Request.q.sender.name == name))
	
	return result._get__dict

def answerRequest(isApproved, request_id):
	# Approves or denies the given request
	r = Request.select(Request.q.id == request_id)
	r.isApproved = isApproved	

def addShiftBlock(startTime, endTime):
	# Creates a new shift
	s = Shift(startTime = startTime, endTime = endTime)

def addNewEmployee(name, isManager, loginPassword, store_id):
	# Creates a new employee
	e = Employee(name=name, isManager=isManager, login=login)
	if (store_id < 0):
		for store in Store.select():
			store.addEmployee(e)
	else:
		store = Store.select(Store.q.id == store_id)[0]
		store.addEmployee(e)
		
	
def fireEmployee(name):
	# Removes an employee
	Employee.delete(Employee.q.name == name)
	
def loadEmployeeList(storeName):
	# Returns a list of employees at a given store
	result = Employee.select(Employee.q.stores == storeName)
	return result

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
