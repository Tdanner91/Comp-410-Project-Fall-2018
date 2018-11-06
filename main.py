from flask import Flask, render_template, request, jsonify
from importlib import import_module
from __selectionPanelToolBox import loadDeviceList as ldl
from __selectionPanelToolBox import loadTestCaseNames as ltcn
import os

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

    


if __name__ == '__main__':
    app.run(debug=True)