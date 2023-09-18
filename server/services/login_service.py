from models.model import User, db, Cart
from flask import request
from flask import jsonify
from flask_jwt_extended import create_access_token
from flask import Blueprint
from flask_jwt_extended import jwt_required, get_jwt_identity

auth_bp = Blueprint('auth', __name__)

@auth_bp.route('/login', methods=['POST'], strict_slashes=False)
def login():
    username = request.json.get('username')
    user = User.query.filter_by(username=username).first()
    if user:
        access_token = create_access_token(identity=username)
        return jsonify({"token": access_token}), 200
    else:
        return jsonify({"message": "Échec de la connexion"}), 401

@auth_bp.route('/register', methods=['POST'], strict_slashes=False)
def register():
    username = request.json.get('username')
    user = User.query.filter_by(username=username).first()

    if not user:
        new_user = User(username=username, admin=0)
        db.session.add(new_user)
        db.session.commit()
        cart = Cart(user_id=new_user.id)
        db.session.add(cart)
        db.session.commit()
        return jsonify({"message": "Inscription réussie"}), 200
    else:
        return jsonify({"message": "Échec register"}), 401

@auth_bp.route('/auth', methods=['GET'])
@jwt_required()  
def is_authenticate():
    username = get_jwt_identity()
    current_user = User.query.filter_by(username=username).first()
    if current_user:
        return jsonify({"authenticated": True}), 200
    else:
        return jsonify({"authenticated": False}), 401

@auth_bp.route('/isAdmin', methods=['GET'])
@jwt_required()  
def is_admin():
    username = get_jwt_identity()
    current_user = User.query.filter_by(username=username).first()
    if current_user and current_user.admin == 1:
        return jsonify({"message": "est admin"}), 200
    else:
        return jsonify({"message": "n'est pas admin"}), 401