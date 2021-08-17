from app import app
from flask import render_template

@app.route("/index", methods = ['GET'])
@app.route("/")
def index():
    return render_template('index.html')

@app.route("/graficos_1")
def grafico():
    return "Parte do grafico"