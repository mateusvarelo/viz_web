"""Inicialização do app Flask """
from flask import Flask



def init_app():
    """Construção do núcleo da aplicação Flask com Dash APP embutido."""
    app = Flask(__name__,instance_relative_config=False)
    app.config.from_object('config')
    
    with app.app_context():
        # Importe do controle de rotas do app flask
        from app.controllers import routes
       
        
        # Importe do app dash
        from .models.dashboard import init_dashboard
        
        #Cria o app flask com dash app embutido 
        app = init_dashboard(app)        
        
        
        return app
app = init_app()    
