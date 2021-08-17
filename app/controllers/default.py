from app import app

@app.route("/index", methods = ['GET'])
@app.route("/")
def index():
    return "Hello word!"

@app.route("/graficos")
def grafico():
    return "Parte do grafico"