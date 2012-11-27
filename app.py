from bottle import Bottle, run, template
from controller import *
from sqlobject import *
from json import *
import jsonpickle
import json
import sys, os


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
@app.get("/hello")
def hello():
	return "Hello World!"

@app.get("/testConstructor")
def get():
	jane=Employee(name="jane",isManager=False,login="5464")	
	
	return to_dict(jane)

run (app,host="localhost", port=8080)

