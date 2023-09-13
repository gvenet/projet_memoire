from flask import Flask
from flask_migrate import Migrate
from services.product_service import produits_bp
from services.login_service import auth_bp
from services.cart_service import cart_bp
from models.model import db
from flask_cors import CORS
from flask_jwt_extended import JWTManager


# init de l'application avec :
# CORS : CORS est un mécanisme de sécurité côté client qui permet de 
# gérer les requêtes HTTP entre différents domaines.
# 
# Migrate :  extension pour Flask qui facilite la gestion des
# migrations de base de données
# 
# JWTManager : extension pour Flask qui facilite la gestion 
# de l'authentification basée sur les JSON Web Tokens (JWT)
#
# Blueprints : moyen d'organiser et de structurer l'application 
# web en plusieurs modules ou composants réutilisables
#
# config : le fichier de configuration Flask
def create_app():
    app = Flask(__name__)  # flask app object
    app.config.from_object('config')

    db.init_app(app)  # Initializing the database

    CORS(app)
    Migrate(app, db)
    JWTManager(app)
    
    app.register_blueprint(produits_bp)
    app.register_blueprint(auth_bp)
    app.register_blueprint(cart_bp)
    
    return app

app = create_app()

if __name__ == '__main__':
    app.run(port=5001)

# # Initialisation de l'application Flask

