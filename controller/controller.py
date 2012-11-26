from model import *

def checkLogin(name, login):


def getMonthDetails(date):


def loadSchedule(employee_id):


def checkSchedule(date):


def loadNotifications(name):


def loadRequests(name):


def answerRequest(isApproved):


def addShiftBlock(startTime, endTime):


def addEmployee(name, isManager, loginPassword, store_id):
	# Creates a new employee
	e = Employee()
	e.name = name
	e.isManager = isManager
	e.login = login
	e.stores.insert(store_id)

def loadEmployeeList(storeName):


def loadStoreList:


def loadTemplateShifts:


def removeShiftBlock(shift_id):


def addEmployeeToShift(employee, shift_id):
	# Adds the given employee to the given shift
	shift_id.employee = employee

def checkAvailableEmployees(shift_id):


def addShiftToDay(shift_id, day_id):
	# Adds the given shift to the given day
	day_id.addShift(shift_id)

def removeShiftFromDay(shift_id, day_id):
	# Removes the given shift from the given day
	day_id.removeShift(shift_id)

def loadDay(day_id):


def addUnavailableDay(day_id):


def removeUnavailableDay(day_id):


def getScheduleDeadline:


def setScheduleDeadline(date):


def addTimeOffRequest(employee_id, date):


def viewNotification(isSeen):

