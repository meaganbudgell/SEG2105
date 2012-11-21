from bottle import Bottle, run, template
from controller import *
from sqlobject import *
import sys, os

#Setup Database Connection <Currently Setup for Meagan's Comp>
connection = connectionForURI("mysql://root:scr33m0@localhost/SEG2105")
sqlhub.processConnection= connection
sqlhub.processConnection.debug = True; sqlhub.processConnection.debugOutput=True
#Creating DB Tables if DNE
for i in (Notification, Employee, Request, TimeOff, Shift, Schedule, Store):
	i.createTable(ifNotExists=True)

#Setting up Devel Server
app=Bottle()

#Test Page
@app.get("/hello")
def hello():
	return "Hello World!"

run (app,host="localhost", port=8080)

