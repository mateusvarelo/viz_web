#from app import app
from flask import render_template
from flask import current_app as app

    
@app.route("/home", methods = ['GET'])
@app.route("/")
def home():
    return render_template('home.html')


@app.route("/grafico_turno", methods = ['GET'])
@app.route("/grafico_turno")
def grafico_turno():
    return render_template('grafico_turno.html')