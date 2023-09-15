from flask import Flask
from flask_migrate import Migrate
from services.product_service import produits_bp
from services.login_service import auth_bp
from services.cart_service import cart_bp
from models.model import db
from flask_cors import CORS
from flask_jwt_extended import JWTManager

def create_app():
    app = Flask(__name__) 
    app.config.from_object('config')

    db.init_app(app)

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


