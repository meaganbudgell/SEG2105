from model import *
import calendar

def addDayToShift(shift_id, day):
	shift=Shift.select(Shift.q.id==shift_id)[0]
	shift.addDay(day)

def addEmployeeToShift(shift_id, eName):
	employee=Employee.select(Employee.q.name==eName)[0]
	shift=Shift.select(Shift.q.id==shift_id)[0]
	shift.addEmployee(employee)

def addEmployeeToStore(sName, eName):
	store = Store.select(Store.q.name == sName)[0]
	employee=Employee.select(Employee.q.name==eName)[0]
	store.addEmployee(employee.id)

def addTemplateShift(inputStartTime, inputEndTime):
	s = Shift(startTime = inputStartTime, endTime = inputEndTime, employee = None, day=None)

def addTimeOffRequest(employee_id, date):
	r = TimeOff(day = date.timetuple().tm_yday, sender = employee_id)

def addUnavailableDay(day_id, employeeName):
	employeeID= Employee.select(Employee.q.name==employeeName)[0]
	ud = UnavailableDay(day = day_id, employee=employeeID.id)

def answerRequest(request_id, answer):
	request= Request.select(Request.q.id==request_id)[0]
	request.answer(answer)

def checkAvailableEmployees(shift_id):	
	s = Shift.select(Shift.q.id == shift_id)[0]
	d = s.day
	
	available = []
	for x in Employee.select():
		for i in x.unavailableDays:
			if i.day_id == d:
				break
		available.insert(x)
	
	result = dict()
	result["items"] = [x.dict for x in available]
	
	return result

def checkDaySchedule(day_id, store):
	try:	
		s = Shift.select(Shift.q.day == day_id, Shift.q.store==store, orderByClass.q.startTime)
		return store.checkSchedule(s)
	except IndexError, e:
		return None

def checkEmployeeLogin(eName, loginCode):
	employee= Employee.select(Employee.q.name==employeeName)[0]
	return employee.checkLogin(loginCode)

def checkSchedule(date,storeName):
	pyDate=datetime.datetime.strptime(date, '%Y-%m-%dT%H:%M:%S.%fZ')
	monthName = pyDate.strftime('%B')
	firstOfMonth = pyDate.replace(day=1)
	lastOfMonth = firstOfMonth.replace(month=pyDate.month+1) - datetime.timedelta(days=1)
	firstOfMonthDayInYear = int(firstOfMonth.strftime('%j'))
	lastOfMonthDayInYear = int(lastOfMonth.strftime('%j'))
	firstOfMonthWeekDay = int(firstOfMonth.strftime('%w'))


def fireEmployee(name):
	Employee.delete(Employee.q.name == name)

def hireEmployee(name, isManager, loginPassword, storeName):
	e = Employee(name=name, isManager=isManager, login=loginPassword)
	if (storeName==None):
		for store in Store.select():
			store.addEmployee(e)
	else:
		store = Store.select(Store.q.name == storeName)[0]
		store.addEmployee(e)

def loadNotifications(employeeName):
	employee = Employee.select(Employee.q.name == employeeName)
	result = dict()
	result["items"] = [x.dict for x in employee.notifications]
	return result	

def loadRequests(name):
	employee = Employee.select(Employee.q.name == employeeName)
	result = dict()
	result["items"] = [x.dict for x in employee.requests]
	return result

def loadSchedule(employeeName):
	shiftList=Shift.select(Shift.q.employee == employee.id)
	result["items"]= [x.dict for x in shiftList]
	return result

def loadStoreEmployees(storeName):
	store = Store.select(Store.q.name == storeName)[0]
	result = dict()
	result["items"]=[x.dict for x in store.employees]
	return result

def loadScheduleDeadline():
	return Store.deadline["deadline"]

def loadStoreList():
	storeList=Store.select()
	result=dict()
	result["items"]=[x.dict for x in storeList]
	return result

def loadTemplateShifts():
	shift = Shift.select(Shift.q.employee == None,Shift.q.day == None)
	result = dict()
	result["items"] = [x.dict for x in shift]
	return result

def matchEmployeeName(employeeName):
	try:
		employee = Employee.select(Employee.q.name == employeeName)[0]
		return employee
	except IndexError, e:
		return None

def removeDayFromShift(shift_id, day):
	shift=Shift.select(Shift.q.id==shift_id)[0]
	shift.removeDay(day)

def removeEmployeeFromShift(shift_id, eName):
	employee=Employee.select(Employee.q.name==eName)[0]
	shift=Shift.select(Shift.q.id==shift_id)[0]
	shift.removeEmployee(employee)

def removeEmployeeFromStore(sName, eName):
	store = Store.select(Store.q.name == sName)[0]
	employee=Employee.select(Employee.q.name==eName)[0]
	store.removeEmployee(employee.id)

def removeTemplateShift(shift_id):
	shift = Shift.select(Shift.q.id == shift_id, Shift.q.day==None)[0]
	shift.destroySelf()

def removeUnavailableDay(day_id, employeeName):
	employeeID= Employee.select(Employee.q.name==employeeName)[0]
	ud = UnavailableDay.select(UnavailableDay.q.day == day_id, UnavailableDay.q.employee==employeeID.id)[0]
	ud.destroySelf()

def setScheduleDeadline(date):
	Store.deadline["deadline"] = date

def viewNotification (notification_id):
	notification= Notification.select(Notification.q.id==notification_id)[0]





