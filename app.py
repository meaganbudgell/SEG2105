from bottle import Bottle, run, template,view
from controller import *
from sqlobject import *
from model import *
import model
import sys, os

#Setup Database Connection <Currently Setup for Meagan's Comp>
connection = connectionForURI("mysql://root:scr33m0@localhost/SEG2105")
sqlhub.processConnection= connection
sqlhub.processConnection.debug = True; sqlhub.processConnection.debugOutput=True

#Creating DB Tables if DNE, runs multiple times to fix ordering.
done = False
while not done:
	try:
		for i in (Employee, Notification, Request, TimeOff, Shift, UnavailableDay, Store):
			i.createTable(ifNotExists=True)
		done = True
	except:
		pass

#Setting up Devel Server
app=Bottle()

#Test Page
@app.get("/testPage")
@view("testPage")
def functionTester():
	for i in (TimeOff, Request, Notification, Shift,UnavailableDay,Employee , Store):	
		for x in i.select():
			x.destroySelf()
	return dict(controller=controller, model=model)

run (app,host="localhost", port=8080)

