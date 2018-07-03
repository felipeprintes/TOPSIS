from flask import Flask, request, render_template, url_for, redirect, send_from_directory
from codPython import TopSis as tp

app = Flask(__name__)

@app.route('/')
def index():
	return render_template('index.html')

@app.route('/pesos', methods=['POST',])
def pesos():
	file = request.files['arquivo'] #tratamento
	#file.save(file.filename)
	df = tp.calcule(file)
	return render_template('pesos.html',pesos=[df.to_html(classes='male')],
		titles = []) 

#@app.route('/teste', methods=['POST',])
#def teste():
	

app.run(debug=True)
