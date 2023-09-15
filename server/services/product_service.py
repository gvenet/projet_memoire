from models.model import db, Product
from flask import jsonify
from flask import Blueprint
from flask_jwt_extended import jwt_required

produits_bp = Blueprint('produits', __name__, url_prefix='/produits')

from models.model import db, Product
from flask import jsonify
from flask import Blueprint
from flask_jwt_extended import jwt_required

produits_bp = Blueprint('produits', __name__, url_prefix='/produits')

@produits_bp.route('/', methods=['GET'], strict_slashes=False)
@jwt_required()
def get_products():
    produits = Product.query.all()
    produits_list = [{
        "id": produit.id, 
        "nom": produit.nom, 
        "prix": float(produit.prix), 
        "description": produit.description, 
        "image_url": produit.image_url
    } for produit in produits]
    return jsonify(produits_list)

@produits_bp.route('/<int:produit_id>', methods=['GET'], strict_slashes=False)
@jwt_required()
def get_product(produit_id):
    produit = Product.query.get(produit_id)
    if produit is None:
        return {'message': 'Le produit spécifié n\'existe pas'}, 404
    produit_data = {
        "id": produit.id, 
        "nom": produit.nom, 
        "prix": float(produit.prix), 
        "description": produit.description, 
        "image_url": produit.image_url
    }
    return jsonify(produit_data)





