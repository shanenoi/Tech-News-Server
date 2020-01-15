from flask import *

import json
import os
import time


APP = Flask(__name__)
DB = "./data.db"
DATA = {}


def save():
	print("[+] Data saved!")
	with open(DB, 'w') as f:
		f.write(str(DATA))



@APP.route("/<collection_name>", methods=["GET", "POST", "PUT", "DELETE"])
def fetch_all(collection_name):

	global DATA

	if request.method == "GET":

		return json.dumps(DATA), 200

	elif request.method == "POST":

		if collection_name in DATA.keys():
			if request.form['key'] not in DATA[collection_name].keys():
				DATA[collection_name][request.form['key']] = [request.form['value'], time.time()]
				save()
				return '{"done!"}', 200
			else:
				return '{"key was created with other value!"}', 500
		else:
			DATA[collection_name] = {}
			DATA[collection_name][request.form['key']] = [request.form['value'], time.time()]
			save()
			return '{"done!"}', 200


	elif request.method == "PUT":

		if collection_name in DATA.keys():
			if request.form['key'] in DATA[collection_name].keys():
				DATA[collection_name][request.form['key']] = [request.form['value'], time.time()]
				save()
				return '{"done!"}', 200
			else:
				return '{"key not found!"}', 500
		else:
			return '{"collection not found!"}', 500

	elif request.method == "DELETE":

		if collection_name in DATA.keys():
			if request.form['key'] in DATA[collection_name].keys():
				del DATA[collection_name][request.form['key']]
				save()
				return '{"done!"}', 200
			else:
				return '{"key not found!"}', 500
		else:
			return '{"collection not found!"}', 500



if __name__ == "__main__":

	try:
		with open(DB) as f:
			DATA = eval(f.read())
	except:
		pass

	APP.run()