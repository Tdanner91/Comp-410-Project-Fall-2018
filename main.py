from flask import Flask, render_template, request, jsonify
from importlib import import_module, invalidate_caches
import databaseFunctions

app = Flask(__name__)

@app.route("/")
@app.route("/home")
def home():
    return render_template('home.html')


@app.route('/process', methods=['POST'])
def process():
	#clears caches so newer test case modules can be found
	invalidate_caches()

	test_case_name = request.form['test_case_js']
	test_code = request.form['test_code_js']
	test_case_repository = 'test_case_repository'
	test_case_run = 'run_test'
	
	#this part took forever but, basically, with import_module you pass to it first the name of the package (the folder containing the module)
	#and then the module (in this case, the test case name), once the module is imported, you can call methods in the module

	test_case = import_module('{}.{}'.format(test_case_repository, test_case_name))
		
	return jsonify({'test_code_returned' : test_case.run_test(test_code)})

@app.route('/databaseFunctions', methods=['POST'])
def databaseFunctions():
	
	return jsonify({'value': 'it worked'})


if __name__ == '__main__':
    app.run(debug=True)