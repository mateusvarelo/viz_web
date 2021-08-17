from app import app

@app.route("/index", methods = ['GET'])
@app.route("/")
def index():
    return "Hello word!"

@app.route("/teste",defaults = {'nome': None})
@app.route("/teste/<nome>")
def teste(nome):
    if nome:
       return f"Oi Sr.{nome}"
    else:
       return f"Oi, sem nome" 