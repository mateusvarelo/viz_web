#Rotas flask
from flask import render_template
from flask import current_app as app

#Padrão    
@app.route("/", methods = ['GET'])
def home():
    return render_template('home.html')
#Detalhe, como podemos observar, não foi criado rota para a pagina dashboard, como foi feito uma conexão entre flask app e dash app, não precisa informar para flask como rotas