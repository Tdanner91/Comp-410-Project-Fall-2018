from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

@app.route('/')
def index():
	return render_template('form.html')

@app.route('/process', methods=['POST'])
def process():

	num1 = request.form['num1']
	num2 = request.form['num2']

	if num1 and num2:
		sum = int(num1) + int(num2)

		return jsonify({'sum' : sum})

	return jsonify({'error' : 'Missing data!'})

if __name__ == '__main__':
    app.run()