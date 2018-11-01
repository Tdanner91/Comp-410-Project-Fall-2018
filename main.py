from flask import Flask, render_template, request, jsonify
from importlib import import_module
import repoCrawler as rc

app = Flask(__name__)

@app.route("/")
@app.route("/home")
def home():
    return render_template('home.html')


@app.route('/selectionPanelResponse', methods=['POST'])
def selectionPanelResponse():
	repoName = request.form['repository']
	data = rc.folderCrawler(repoName)
	
	return jsonify(data)




if __name__ == '__main__':
    app.run(debug=True)