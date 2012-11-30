from bottle import Bottle, run, template,view, default_app,route, static_file

from sqlobject import *
from model import *
import model
import sys, os
import bottle
bottle.debug(True)

#Setup Database Connection <Currently Setup for Meagan's Comp>
connection = connectionForURI("mysql://root:jordan13@localhost/SEG2105")
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

from controller import *

@app.route("/index")
def function():
	return static_file("index.html", root='./views')

@app.route("/static/<extension>/<filename>")
def serveStatic(extension,filename):
	x=extension
	x+='/'
	x+=filename	
	return static_file(x, root = "./views")
#Test Page
#@app.get("/testPage")
#@view("testPage")
#def functionTester():
#	for i in (TimeOff, Request, Notification, Shift,UnavailableDay,Employee , Store):	
#		for x in i.select():
#			x.destroySelf()
#	return dict(controller=controller, model=model)

run (app,host="localhost", port=8080)

