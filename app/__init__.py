from flask import Flask

#app = Flask(__name__)
def init_app():
    
    app.config.from_object('config')

from app.controllers import routes