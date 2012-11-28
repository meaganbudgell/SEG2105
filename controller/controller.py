from model import *
import calendar
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
	pyDate=datetime.strptime(date, '%Y-%m-%dT%H:%M:%S.%fZ')
	monthName=calendar.month_name(pyDate.date.month())
	dayNameStart=pyDate.date.weekday()

def loadSchedule(employeeName):
	# Returns every shift that an employee works

	shiftList=Shift.select(Shift.q.employee == employee.id)
	result["items"]= [x.dict for x in shiftList]
	return result

def checkSchedule(date):
	# Returns True if the date is filled, False otherwise
	
	day_id = date.timetuple().tm_yday
	
	try:
		s = Shift.select(Shift.q.day == day_id)[0]
		return True
	except IndexError, e:
		return False
	
	
def matchEmployeeName(employeeName):
	try:
		employee = Employee.select(Employee.q.name == employeeName)[0]
		return employee
	except IndexError, e:
		return None

def loadNotifications(employeeName):
	# Return all of the notifications of the given employee
	employee = Employee.select(Employee.q.name == employeeName)
	result = dict()
	result["items"] = [x.dict for x in employee.notifications]
	return result
	

def loadRequests(name):
	# Return all of the requests of the given employee
	employee = Employee.select(Employee.q.name == employeeName)
	result = dict()
	result["items"] = [x.dict for x in employee.requests]
	return result

def answerRequest(isApproved, request_id):
	# Approves or denies the given request
	r = Request.select(Request.q.id == request_id)
	r.isApproved = isApproved	

def addTemplateShift(inputStartTime, inputEndTime):
	# Creates a new shift
	s = Shift(startTime = inputStartTime, endTime = inputEndTime, employee = None, day=None)

def addNewEmployee(name, isManager, loginPassword, storeName):
	# Creates a new employee
	e = Employee(name=name, isManager=isManager, login=loginPassword)
	if (storeName==None):
		for store in Store.select():
			store.addEmployee(e)
	else:
		store = Store.select(Store.q.name == storeName)[0]
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
	# Returns all of the shifts that DO NOT have an Employee
	shift = Shift.select(Shift.q.employee == None)
	result = dict()
	result["items"] = [x.dict for x in shift]
	return result

def addEmployeeToStore(sName, eName):
	store = Store.select(Store.q.name == sName)[0]
	employee=Employee.select(Employee.q.name==eName)[0]
	store.addEmployee(employee.id)

def removeEmployeeFromStore(sName, eName):
	store = Store.select(Store.q.name == sName)[0]
	employee=Employee.select(Employee.q.name==eName)[0]
	store.removeEmployee(employee.id)

def removeTemplateShift(shift_id):
	shift = Shift.select(Shift.q.id == shift_id, Shift.q.day==None)[0]
	shift.destroySelf()

def addEmployeeToShift(eName, shift_id):
	# Adds the given employee to the given shift
	employee=Employee.select(Employee.q.name==eName)[0]
	shift = Shift.select(Shift.q.id == shift_id)[0]

def checkAvailableEmployees(shift_id):
	# Returns a list of employees who are free for a given shift
	
	# Get the shift and the day that corresponds to it
	s = Shift.select(Shift.q.id == shift_id)[0]
	d = s.day
	
	available = []
	
	# Get a list of all of the employees and get the employees from the unavailable days
	for x in Employee.select():
		for i in x.unavailableDays:
			if i.day_id == d:
				break
			
		# If we made it here we can add the employee to the list
		available.insert(x)
	
	result = dict()
	result["items"] = [x.dict for x in available]
	
	return result

def addDayToShift(shift_id, day_id):
	Shift.select(Shift.q.id==shift_id)[0].day=day_id

def removeDayFromShift(shift_id):
	Shift.select(Shift.q.id==shift_id)[0].destroySelf()

def addUnavailableDay(day_id, employeeName):
	# Creates a new UnavailableDay
	employeeID= Employee.select(Employee.q.name==employeeName)[0]
	ud = UnavailableDay(day = day_id, employee=employeeID.id)

def removeUnavailableDay(day_id, employeeName):
	# Removes the specified day
	employeeID= Employee.select(Employee.q.name==employeeName)[0]
	ud = UnavailableDay.select(UnavailableDay.q.day == day_id, UnavailableDay.q.employee==employeeID.id)[0]
	ud.destroySelf()

def getScheduleDeadline():
	# Returns the deadline set for employees to modify their personal schedule
	return Store.deadline["deadline"]

def setScheduleDeadline(date):
	Store.deadline["deadline"] = date

def addTimeOffRequest(employee_id, date):
	# Creates a new TimeOff Request
	r = TimeOff(day = date.timetuple().tm_yday, sender = employee_id)

def viewNotification(isSeen, notification_id):
	# Sets a notification's status to "viewed"
	n = Notification.select(notification_id)[0]
	n.isSees = isSeen
	return n._get_dict
