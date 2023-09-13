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

# Écoute sur localhost/produits
@produits_bp.route('/', methods=['GET'], strict_slashes=False)
# Utilise la décoration jwt_required pour exiger une authentification par JWT
# Le token est envoyé par le client dans l'en-tête de la requête
@jwt_required()
def get_products():
    # Récupération de tous les produits en base de données
    produits = Product.query.all()
    # Création d'une liste de produits
    produits_list = [{
        "id": produit.id, 
        "nom": produit.nom, 
        "prix": float(produit.prix), 
        "description": produit.description, 
        "image_url": produit.image_url
    } for produit in produits]
    # Retour de la liste au format JSON
    return jsonify(produits_list)

# Écoute sur localhost/produits/:id
@produits_bp.route('/<int:produit_id>', methods=['GET'], strict_slashes=False)
@jwt_required()
def get_product(produit_id):
    # On récupère le produit correspondant à l'id
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



