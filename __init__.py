import flask
from flask import Flask,render_template,request,redirect,jsonify,url_for
import os, sys
#import unicodedata
from os import environ

app = Flask(__name__)
app.debug=True

@app.route('/')
#@app.route("/index")
def index():
	return render_template('index.html')

@app.route('/dipe')
def dipe():
	return render_template('dipe.html')

@app.route('/uploaddipe', methods=['GET', 'POST'])	
def uploaddipe():
	if request.method == 'POST':
		_file = request.files['uploadedfile']
	return _file.filename
	
	

if __name__ == '__main__':
	host= environ.get('SERVER_HOST', 'localhost')
	try:
		port = int(environ.get('SERVER_PORT', '50015'))
	except ValueError:
		port = 5000
	
	app.run(host , port)
