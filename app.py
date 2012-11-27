from bottle import Bottle, run, template, static_file
from controller import *
from sqlobject import *
import logging
import sys, os

#Logging Config
logging.basicConfig(filename='logs/log.txt')

#Setup Database Connection <Currently Setup for Meagan's Comp>
connection = connectionForURI("mysql://root:scr33m0@localhost/SEG2105")
sqlhub.processConnection= connection
sqlhub.processConnection.debug = True; sqlhub.processConnection.debugOutput=True

#Creating DB Tables if DNE, runs multiple times to fix ordering.
done = False
while not done:
	try:
		for i in (Employee, Notification, Request, TimeOff, Shift, Day, UnavailableDay, Store):
			i.createTable(ifNotExists=True)
		done = True
	except:
		pass

#Setting up Devel Server
app=Bottle()

#Test Page
@app.get("/testPage")
def functionTester():
	jane=Employee(name="Jane", isManager=True, login="4126")
	logging.debug("Created Jane")
	logging.debug(controller.toDict(jane))
	tim=Employee(name="Tim", isManager=False, login="4189")
	logging.debug("Created Tim")
	logging.debug(controller.toDict(tim))
	bob=Employee(name="Bob", isManager=False, login="4122")
	logging.debug("Created Bob")
	logging.debug(controller.toDict(bob))
	peter=Employee(name="Peter", isManager=False, login="4121")
	logging.debug("Created Peter")
	logging.debug(controller.toDict(peter))
	abcStore=Store(name="ABC")
	logging.debug("Created ABC Store")
	logging.debug(controller.toDict(abcStore))
			


	return static_file("log.txt", root="logs/log.txt")

run (app,host="localhost", port=8080)

