from models.model import User, db, Cart
from flask import request
from flask import jsonify
from flask_jwt_extended import create_access_token
from flask import Blueprint
from flask_jwt_extended import jwt_required, get_jwt_identity

auth_bp = Blueprint('auth', __name__)

# Ecoute sur localhost/5001/login avec POST
@auth_bp.route('/login', methods=['POST'], strict_slashes=False)
def login():
    # Récupère le nom d'utilisateur depuis les données JSON de la requête
    username = request.json.get('username')
    # Recherche l'utilisateur dans la base de données par son nom d'utilisateur
    user = User.query.filter_by(username=username).first()
    if user:
         # Utilise Flask-JWT-Extended pour générer un jeton d'accès
        access_token = create_access_token(identity=username)
        # Retourne le jeton d'accès et l'identifiant de l'utilisateur en tant que réponse JSON
        return jsonify({"token": access_token}), 200
    else:
        return jsonify({"message": "Échec de la connexion"}), 401

# Ecoute sur localhost/5001/register avec POST
@auth_bp.route('/register', methods=['POST'], strict_slashes=False)
def register():
    username = request.json.get('username')
    user = User.query.filter_by(username=username).first()

    if not user:
        # Si l'utilisateur n'existe pas, crée un nouvel utilisateur avec le nom d'utilisateur fourni
        new_user = User(username=username)
        # Ajoute le nouvel utilisateur à la session de base de données et effectue la sauvegarde
        db.session.add(new_user)
        db.session.commit()
        # Crée un panier par défaut pour le nouvel utilisateur
        cart = Cart(user_id=new_user.id)
        # Ajoute le panier à la session de base de données et effectue la sauvegarde
        db.session.add(cart)
        db.session.commit()
        return jsonify({"message": "Inscription réussie"}), 200
    else:
        return jsonify({"message": "Échec register"}), 401

@auth_bp.route('/auth', methods=['GET'])
@jwt_required()  # Requiert une authentification via JWT
def is_authenticate():
    username = get_jwt_identity()
    # Recherche de l'utilisateur dans la base de données en utilisant le nom d'utilisateur
    current_user = User.query.filter_by(username=username).first()
    if current_user:
        return jsonify({"authenticated": True}), 200
    else:
        return jsonify({"authenticated": False}), 401