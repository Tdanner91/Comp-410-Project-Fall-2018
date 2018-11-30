from flask import Flask, render_template, request, jsonify
from importlib import import_module
from __selectionPanelToolBox import loadDeviceList as ldl
from __selectionPanelToolBox import loadTestCaseNames as ltcn
import os, json, queue, threading, time, datetime, sqlite3
from multiprocessing import Process, Queue
import subprocess

app = Flask(__name__)

@app.route("/")
@app.route("/home")
def home():
	return render_template('home.html')


@app.route('/selectionPanelResponse', methods=['POST'])
def selectionPanelResponse():
	repoName = request.form['repository']

	if repoName == 'device_repository':
		data = ldl.loadDeviceList()
		return jsonify(data)

	elif repoName == 'test_case_repository':
		data = ltcn.loadTestCaseNames()
		return jsonify(data)
	elif repoName == 'saved_results':
		pass

@app.route('/userGeneratedScriptUploading', methods=['POST'])
def userGeneratedScriptUploading():
	script = request.form['_script']
	scriptName = request.form['_scriptName'] + '.py'
	returnScriptName = scriptName
	subdirectory = '__test_case_repository'

	scriptName = os.path.join(subdirectory, scriptName)

	scriptWriter = open(scriptName, 'w')
	scriptWriter.write(script)
	scriptWriter.close()

	return jsonify({'name' : returnScriptName})

@app.route('/removeScriptsFromRepo', methods=['POST'])
def removeScriptsFromRepo():
	scriptsList = json.loads(request.form['scriptslist'])
	for i in range(len(scriptsList)):
		os.remove("__test_case_repository/" + scriptsList[i])

	
	return jsonify({'ret' : scriptsList})

@app.route('/updateDatabase', methods=['POST'])
def updateDatabase():
	data = []

	conn = sqlite3.connect('SavedResults.db')
	c = conn.cursor()

	for row in c.execute('SELECT * FROM results'):
    		data.append(row)

	return jsonify({'database': data})

############################Execution Queue############################
execQ = Queue()
execList = []
@app.route('/executeScripts', methods=['POST'])
def executeScripts():
	scriptsList = json.loads(request.form['scriptslist'])
	for script in scriptsList:
		execQ.put(script)
		execList.append(script)

	return jsonify({'ret' : execList})

databaseResults = {}

def executioner():

	while True:
		time.sleep(5)
		if execQ.empty():
			pass
		else:
			conn = sqlite3.connect('SavedResults.db')
			c = conn.cursor()
			
			dt = datetime.datetime.now()
			test_date_time = '{:%a %m/%d/%y %H:%M %p}'.format(dt)
			testName = execQ.get()
			results_name = ''
			
			try:
				pass_fail = 'pass'
				os.system('python __test_case_repository/' + testName)
				print('Test Done!!!')
			except:
				pass_fail = 'fail'
				print('ERROR!!!')
			
			c.execute('INSERT INTO results (date_time, test_name, pass_fail, results_name) VALUES (?, ?, ?, ?)', (test_date_time, testName, pass_fail, results_name))
			
			conn.commit()
			c.close()
			conn.close()
			print('database updated')

if __name__ == '__main__':
	t = threading.Thread(target=executioner)
	t.daemon = True
	t.start()
	app.run(threaded=True, debug=True)
	