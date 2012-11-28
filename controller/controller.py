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

def loadSchedule(employeeName):
	# Returns every shift that an employee works

	shiftList=Shift.select(Shift.q.employee == employee.id)
	result["items"]= [x.dict for x in shiftList]
	return result

def checkSchedule(date):
	pass
def matchEmployeeName(employeeName):
	try:
		employee = Employee.select(Employee.q.name == employeeName)[0]
		return employee
	except IndexError, e:
		return None

def loadNotifications(employeeName):
	# Return all of the notifications
	pass

def loadRequests(name):
	# Return all of the requests	
	result = Request.select()	
	return toDict(result)

def answerRequest(isApproved, request_id):
	# Approves or denies the given request
	r = Request.select(Request.q.id == request_id)
	r.isApproved = isApproved	

def addShiftBlock(startTime, endTime):
	# Creates a new shift
	s = Shift(startTime = startTime, endTime = endTime)

def addNewEmployee(name, isManager, loginPassword, store_id):
	# Creates a new employee
	e = Employee(name=name, isManager=isManager, login=loginPassword)
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
	store = Store.select(Store.q.name == storeName)[0]
	result = dict()
	result["items"]=[x.dict for x in store.employees]
	return result


def loadStoreList():
	# Returns all of the stores
	storeList=Store.select()
	result=dict()
	result["items"]=[x.dict for x in storeList]
	return result

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

def addUnavailableDay(day_id):
	# Creates a new UnavailableDay
	ud = UnavailableDay(dayNumber = day_id)

def removeUnavailableDay(day_id):
	# Removes the specified day
	ud = UnavailableDay.select(day_id)[0]
	ud.destroySelf()


def getScheduleDeadline():
	# Returns the deadline set for employees to modify their personal schedule
	result = Store.select()[0]
	# NEEDS TO BE FIXED

def setScheduleDeadline(date):
	pass

def addTimeOffRequest(employee_id, date):
	# Creates a new TimeOff Request
	r = TimeOff(day = date.timetuple().tm_yday, sender = employee_id)

def viewNotification(isSeen, notification_id):
	# Sets a notification's status to "viewed"
	n = Notification.select(notification_id)[0]
	n.isSees = isSeen
	return n._get_dict
