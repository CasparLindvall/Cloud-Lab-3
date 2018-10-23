#!flask/bin/python
from flask import Flask, jsonify, request
from tasks import countTweets
import subprocess
import sys

app = Flask(__name__)

@app.route('/', methods=['GET'])
def server():
	time = request.args.get('time', default = 1, type = int)
	data = countTweets.delay(time=time)
	model = data.get(propagate=False)
	return(jsonify(model))

if __name__ == '__main__':
	app.run(host='0.0.0.0',debug=True)
