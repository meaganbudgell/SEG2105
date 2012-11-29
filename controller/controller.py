from model import *
import calendar

def addEmployeeToStore(sName, eName):
	store = Store.select(Store.q.name == sName)[0]
	employee=Employee.select(Employee.q.name==eName)[0]
	store.addEmployee(employee.id)

def addTemplateShift(inputStartTime, inputEndTime):
	# Creates a new shift
	s = Shift(startTime = inputStartTime, endTime = inputEndTime, employee = None, day=None)

def addTimeOffRequest(employee_id, date):
	# Creates a new TimeOff Request
	r = TimeOff(day = date.timetuple().tm_yday, sender = employee_id)

def addUnavailableDay(day_id, employeeName):
	# Creates a new UnavailableDay
	employeeID= Employee.select(Employee.q.name==employeeName)[0]
	ud = UnavailableDay(day = day_id, employee=employeeID.id)

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

def checkDaySchedule(date, storeName):
	pyDate=datetime.strptime(date, '%Y-%m-%dT%H:%M:%S.%fZ')
	day_id = pyDate.timetuple().tm_yday
	try:
		store= Store.select(Store.q.name==storeName)[0]		
		s = Shift.select(Shift.q.day == day_id, Shift.q.store==store, orderByClass.q.startTime)
		return store.checkSchedule(s)
	except IndexError, e:
		return None

def fireEmployee(name):
	# Removes an employee
	Employee.delete(Employee.q.name == name)

def hireEmployee(name, isManager, loginPassword, storeName):
	# Creates a new employee
	e = Employee(name=name, isManager=isManager, login=loginPassword)
	if (storeName==None):
		for store in Store.select():
			store.addEmployee(e)
	else:
		store = Store.select(Store.q.name == storeName)[0]
		store.addEmployee(e)

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

def loadSchedule(employeeName):
	# Returns every shift that an employee works

	shiftList=Shift.select(Shift.q.employee == employee.id)
	result["items"]= [x.dict for x in shiftList]
	return result

def loadStoreEmployees(storeName):
	# Returns a list of employees at a given store
	store = Store.select(Store.q.name == storeName)[0]
	result = dict()
	result["items"]=[x.dict for x in store.employees]
	return result

def loadScheduleDeadline():
	# Returns the deadline set for employees to modify their personal schedule
	return Store.deadline["deadline"]

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

def matchEmployeeName(employeeName):
	try:
		employee = Employee.select(Employee.q.name == employeeName)[0]
		return employee
	except IndexError, e:

def removeEmployeeFromStore(sName, eName):
	store = Store.select(Store.q.name == sName)[0]
	employee=Employee.select(Employee.q.name==eName)[0]
	store.removeEmployee(employee.id)

def removeTemplateShift(shift_id):
	shift = Shift.select(Shift.q.id == shift_id, Shift.q.day==None)[0]
	shift.destroySelf()

def removeUnavailableDay(day_id, employeeName):
	# Removes the specified day
	employeeID= Employee.select(Employee.q.name==employeeName)[0]
	ud = UnavailableDay.select(UnavailableDay.q.day == day_id, UnavailableDay.q.employee==employeeID.id)[0]
	ud.destroySelf()

def setScheduleDeadline(date):
	Store.deadline["deadline"] = date







