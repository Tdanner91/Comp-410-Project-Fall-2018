from flask import Flask, render_template, request, jsonify
from importlib import import_module
from __selectionPanelToolBox import loadDeviceList as ldl
from __selectionPanelToolBox import loadTestCaseNames as ltcn
import os, json, queue


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
    print(scriptsList)
    for i in range(len(scriptsList)):
        os.remove("__test_case_repository/" + scriptsList[i])

    return jsonify({'ret' : scriptsList})


############################Execution Queue############################
execQ = queue.Queue()

@app.route('/executionQueue', methods=['POST'])
def executionQueue():
    pass
    
    def executioner():
        pass

if __name__ == '__main__':
    app.run(debug=True)