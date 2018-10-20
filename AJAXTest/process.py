import subprocess
from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('form.html')

@app.route('/process', methods=['POST'])
def process(script_path):
    result = subprocess.Popen(script_path,
    shell=True,
    stdin=subprocess.PIPE,
    stdout=subprocess.PIPE,
    stderr=subprocess.STDOUT,
    universal_newlines=True)

    result_code = request.form['num1']

    return int(result_code)

    test_result = process(r'Comp-410-Project-Fall-2018/AJAXTest/test_script_mock.py')

# this print is for debug only
    print(str(test_result))

# return jsonify({'sum' : test_result})

    return jsonify({'Result': test_result})

if __name__ == '__main__':
    app.run()
