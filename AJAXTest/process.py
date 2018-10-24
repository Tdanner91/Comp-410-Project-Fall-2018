
from flask import Flask, render_template, request, jsonify
from test_script_mock import my_test_case_mock
app = Flask(__name__)

@app.route('/')
def index():
    return render_template('form.html')

@app.route('/process', methods=['POST'])
def process():
    test_code_processpy = request.form['test_code_js']

    if test_code_processpy:
        return jsonify({'test_code_returned' : my_test_case_mock(test_code_processpy)})


if __name__ == '__main__':
    app.run(debug=True)
