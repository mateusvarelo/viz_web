from app import app
from flask import render_template


    
@app.route("/index", methods = ['GET'])
@app.route("/")
def index():
    return render_template('index.html')

@app.route("/dashboard", methods = ['GET'])
@app.route("/dashboard")
def dashboard():
    return render_template('dashboard.html')

@app.route("/grafico_turno", methods = ['GET'])
@app.route("/grafico_turno")
def grafico_1():
    return render_template('grafico_turno.html')