from model import *
import calendar
import datetime
from bottle import Bottle, run, template,view
import default_app

app=default_app()

@app.post("/addDayToShift/")
def addDayToShift():
	shift_id=request.json.shift_id
	day=request.json.day
	shift=Shift.select(Shift.q.id==shift_id)[0]
	shift.addDay(day)

@app.post("/addEmployeeToShift/")
def addEmployeeToShift():
	shift_id=request.json.shift_id
	eName=request.json.eName
	employee=Employee.select(Employee.q.name==eName)[0]
	shift=Shift.select(Shift.q.id==shift_id)[0]
	shift.addEmployee(employee)

@app.post("/addEmployeeToStore/")
def addEmployeeToStore():
	sName=request.json.sName
	eName=request.json.eName
	store = Store.select(Store.q.name == sName)[0]
	employee=Employee.select(Employee.q.name==eName)[0]
	store.addEmployee(employee.id)

@app.post("/addTemplateShift/")
def addTemplateShift():
	inputStartTime=request.json.inputStartTime
	inputEndTime=request.json.inputEndTime
	s = Shift(startTime = inputStartTime, endTime = inputEndTime, employee = None, day=None)

@app.post("/addTimeOffRequest/")
def addTimeOffRequest():
	eName=request.json.eName
	date=request.json.date
	employee = Employee.select(Employee.q.name==eName)[0]
	r = TimeOff(day = date.timetuple().tm_yday, sender = employee.id)

@app.post("/addUnavailableDay/")
def addUnavailableDay():
	day=request.json.day
	eName=request.json.eName
	employeeID= Employee.select(Employee.q.name==employeeName)[0]
	ud = UnavailableDay(day = day_id, employee=employeeID.id)


@app.post("/answerRequest/")
def answerRequest():
	request_id=request.json.request_id
	answer=request.json.answer
	request= Request.select(Request.q.id==request_id)[0]
	request.answer(answer)


@app.get("/checkAvailableEmployees/")
def checkAvailableEmployees():
	shift_id=request.json.shift_id	
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

#This is only accessible through checkSchedule()
def checkDaySchedule(day, store):
	try:	
		s = Shift.select(Shift.q.day == day_id, Shift.q.store==store, orderByClass.q.startTime)
		return store.checkSchedule(s)
	except IndexError, e:
		return None

@app.get("/checkEmployeeLogin/")
def checkEmployeeLogin():
	eName=request.json.eName
	loginCode=request.json.loginCode
	employee= Employee.select(Employee.q.name==employeeName)[0]
	return employee.checkLogin(loginCode)

@app.get("/checkSchedule/")
def checkSchedule():
	date=request.json.date
	sName=request.json.sName
	pyDate=datetime.datetime.strptime(date, '%Y-%m-%dT%H:%M:%S.%fZ')
	monthName = pyDate.strftime('%B')
	firstOfMonth = pyDate.replace(day=1)
	lastOfMonth = firstOfMonth.replace(month=pyDate.month+1) - datetime.timedelta(days=1)
	firstOfMonthDayInYear = int(firstOfMonth.strftime('%j'))
	lastOfMonthDayInYear = int(lastOfMonth.strftime('%j'))
	firstOfMonthWeekDay = int(firstOfMonth.strftime('%w'))

@app.post("/fireEmployee/")
def fireEmployee():
	eName=request.json.eName
	Employee.delete(Employee.q.name == eName)

@app.post("/hireEmployee/")
def hireEmployee():
	eName=request.json.eName
	isManager=request.json.isManager
	loginCode=request.json.loginCode
	sName=request.json.sName

	e = Employee(name=ename, isManager=isManager, login=loginCode)
	if (storeName==None):
		for store in Store.select():
			store.addEmployee(e)
	else:
		store = Store.select(Store.q.name == sName)[0]
		store.addEmployee(e)

@app.get("/loadNotifications/")
def loadNotifications():

	eName=request.json.eName
	employee = Employee.select(Employee.q.name == employeeName)
	result = dict()
	result["items"] = [x.dict for x in employee.notifications]
	return result	

@app.get("/loadRequests/")
def loadRequests():
	eName=request.json.eName
	employee = Employee.select(Employee.q.name == eName)
	result = dict()
	result["items"] = [x.dict for x in employee.requests]
	return result

@app.get("/loadStoreEmployees/")
def loadStoreEmployees():
	sName=request.json.sName
	store = Store.select(Store.q.name == sName)[0]
	result = dict()
	result["items"]=[x.dict for x in store.employees]
	return result

@app.get("/loadScheduleDeadline/")
def loadScheduleDeadline():
	return Store.deadline["deadline"]

@app.get("/loadStoreList")
def loadStoreList():
	storeList=Store.select()
	result=dict()
	result["items"]=[x.dict for x in storeList]
	return result

@app.get("/loadTemplateShifts/")
def loadTemplateShifts():
	shift = Shift.select(Shift.q.employee == None,Shift.q.day == None)
	result = dict()
	result["items"] = [x.dict for x in shift]
	return result

@app.post("/removeDayFromShift/")
def removeDayFromShift():
	shift_id=request.json.shift_id	
	day=request.json.day
	shift=Shift.select(Shift.q.id==shift_id)[0]
	shift.removeDay(day)

@app.post("/removeEmployeeFromShift/")
def removeEmployeeFromShift():
	shift_id=request.json.shift_id
	eName=request.json.eName
	employee=Employee.select(Employee.q.name==eName)[0]
	shift=Shift.select(Shift.q.id==shift_id)[0]
	shift.removeEmployee(employee)

@app.post("/remobeEmployeeFromStore/")
def removeEmployeeFromStore():
	sName=request.json.sName
	eName=request.json.eName
	store = Store.select(Store.q.name == sName)[0]
	employee=Employee.select(Employee.q.name==eName)[0]
	store.removeEmployee(employee.id)

@app.post("/removeTemplateShift/")
def removeTemplateShift():
	shift_id=request.json.shift_id
	shift = Shift.select(Shift.q.id == shift_id, Shift.q.day==None)[0]
	shift.destroySelf()

@app.post("/removeUnavailableDay/")
def removeUnavailableDay():
	day_id=request.json.day_id
	eName=request.json.eName
	employeeID= Employee.select(Employee.q.name==eName)[0]
	ud = UnavailableDay.select(UnavailableDay.q.day == day_id, UnavailableDay.q.employee==employeeID.id)[0]
	ud.destroySelf()

@app.post("/setScheduleDeadline/")
def setScheduleDeadline():
	date=request.json.date
	Store.deadline["deadline"] = date

@app.post("/viewNotification/")
def viewNotification ():
	notification_id=request.json.notification_id
	notification= Notification.select(Notification.q.id==notification_id)[0]





