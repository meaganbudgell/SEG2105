from model import *

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

def loadStoreList:
	pass

def loadTemplateShifts:
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

def getScheduleDeadline:
	pass

def setScheduleDeadline(date):
	pass

def addTimeOffRequest(employee_id, date):
	pass

def viewNotification(isSeen):
	pass
