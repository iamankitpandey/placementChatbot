from initial import *
from flask import Flask, render_template, request, jsonify
app = Flask(__name__)

@app.route('/')
def hello_world():
    return render_template('index.html')

@app.route('/process', methods=['POST'])
def process():
    data = request.form['data']
    key_pressed = request.form['key_pressed']
    if key_pressed=="enter_key":
    	data = data[0: len(data)-1] #solve for send key
    #algo to start from here
    if data:
    	final_answer = thinking(data)
    	
    	return jsonify({'answer':final_answer})
    else:
    	return jsonify({'answer':"???"})