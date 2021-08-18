from app import app
from flask import render_template

@app.route("/index", methods = ['GET'])
@app.route("/")
def index():
    return render_template('teste.html')

@app.route("/dashboard")
def grafico():
    return render_template('grafico.html')