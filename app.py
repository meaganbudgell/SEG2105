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
	def to_dict(obj):
		# each type of column
		foreigns = obj.sqlmeta._plainForeignGetters.keys()
		joins = obj.sqlmeta.joinDefinitions

		# all of the basic stuff is built-in (as I recently discovered -_- )
		d = obj.sqlmeta.asDict()

		# convert all datetimes/dates/times to something JSON can use
		for k in d:
		       if isinstance(d[k], datetime.datetime) or isinstance(d[k], datetime.date) or isinstance(d[k], datetime.time):
			       d[k] = d[k].isoformat()

		# function given class and list of objects of that class, returns object dict for that reference
		# an object dict is a dictionary with 2 keys.  name is the name of the class that the objects contained are instances of
		# items is the list of IDs referenced.
		def f(klass, objs):
		       return dict(name=klass,
				   items=[x.id for x in objs])

		# convert all foreign keys to one-element object dicts
		for key in foreigns:
		       d.update({key:f(getattr(obj, key)._class_._name_, [getattr(obj, key)])})

		# convert all joins to object dicts
		for key in joins:
		       d.update({key.name:f(key.kw['otherClass'], getattr(obj, key.name))})
       
       		return d
	return json.dump(to_dict(jane))

run (app,host="localhost", port=8080)

