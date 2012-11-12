from bottle import Bottle, run, template
from controller import *
from model import *

app=bottle()

@app.route("/hello")
def hello():
	return "Hello World!"

run (app,host="localhost", port=8080)

