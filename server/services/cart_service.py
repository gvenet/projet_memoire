from flask import Blueprint, request, jsonify
from flask_jwt_extended import jwt_required, get_jwt_identity
from models.model import db, Product, User, Cart, CartItem
from sqlalchemy import func


cart_bp = Blueprint('cart', __name__, url_prefix='/cart')

@cart_bp.route('/products', methods=['GET'])
@jwt_required()  
def get_cart_products():
    username = get_jwt_identity()
    current_user = User.query.filter_by(username=username).first()
    cart = Cart.query.filter_by(user_id=current_user.id).first()

    if cart is None:
        return jsonify({"message": "Le panier spécifié n'existe pas"}), 404

    cart_items = CartItem.query.filter_by(cart_id=cart.id).all()

    cart_products = [{
        "id": item.product.id,
        "nom": item.product.nom,
        "prix": float(item.product.prix),
        "description": item.product.description,
        "image_url": item.product.image_url,
        "quantity": item.quantity,
        "total": item.total_price
    } for item in cart_items]
    
    return jsonify(cart_products), 200

@cart_bp.route('/product/<int:product_id>', methods=['GET'])
@jwt_required()
def get_cart_product(product_id):
    username = get_jwt_identity()
    current_user = User.query.filter_by(username=username).first()

    cart = Cart.query.filter_by(user_id=current_user.id).first()

    if cart is None:
        return jsonify({"message": "Le panier spécifié n'existe pas"}), 404

    cart_item = CartItem.query.filter_by(cart_id=cart.id, product_id=product_id).first()

    if cart_item is None:
        return jsonify({"message": "Le produit spécifié n'existe pas dans le panier"}), 404

    cart_product = {
        "id": cart_item.product.id,
        "nom": cart_item.product.nom,
        "prix": float(cart_item.product.prix),
        "description": cart_item.product.description,
        "image_url": cart_item.product.image_url,
        "quantity": cart_item.quantity,
        "total": cart_item.total_price
    }

    return jsonify(cart_product), 200

@cart_bp.route('/add-product', methods=['POST'])
@jwt_required() 
def add_product_to_cart():
    username = get_jwt_identity()
    current_user = User.query.filter_by(username=username).first()

    if not current_user:
        return jsonify({"message": "Utilisateur non trouvé"}), 404

    data = request.json
    product_id = data.get('productId')
    quantity = data.get('quantity', 1) 
    
    product = Product.query.get(product_id)
    if not product:
        return jsonify({"message": "Produit non trouvé"}), 404

    cart = Cart.query.filter_by(user_id=current_user.id).first()
    if not cart:
        cart = Cart(user_id=current_user.id)
        db.session.add(cart)

    cart_item = CartItem(cart_id=cart.id, product_id=product.id, quantity=quantity, total_price=product.prix * quantity)
    db.session.add(cart_item)
    db.session.commit()

    return jsonify({"message": "Produit ajouté au panier avec succès"}), 200

@cart_bp.route('/update-product', methods=['PUT'])
@jwt_required()
def update_product_in_cart():
    username = get_jwt_identity()

    current_user = User.query.filter_by(username=username).first()

    if not current_user:
        return jsonify({"message": "Utilisateur non trouvé"}), 404

    data = request.json
    quantity = data.get('quantity')
    product_id = data.get('productId')

    product = Product.query.get(product_id)
    if not product:
        return jsonify({"message": "Produit non trouvé"}), 404

    cart = Cart.query.filter_by(user_id=current_user.id).first()
    if not cart:
        return jsonify({"message": "Panier de l'utilisateur non trouvé"}), 404

    cart_item = CartItem.query.filter_by(cart_id=cart.id, product_id=product_id).first()
    if cart_item:
        cart_item.quantity = quantity
        cart_item.total_price = product.prix * quantity
        db.session.commit()
        return jsonify({"message": "Quantité de produit mise à jour avec succès"}), 200
    else:
        return jsonify({"message": "Produit non trouvé dans le panier de l'utilisateur"}), 404

@cart_bp.route('/delete-product/<int:product_id>', methods=['DELETE'])
@jwt_required() 
def delete_product_from_cart(product_id):
    username = get_jwt_identity()

    current_user = User.query.filter_by(username=username).first()

    if not current_user:
        return jsonify({"message": "Utilisateur non trouvé"}), 404

    product = Product.query.get(product_id)
    if not product:
        return jsonify({"message": "Produit non trouvé"}), 404

    cart = Cart.query.filter_by(user_id=current_user.id).first()
    if not cart:
        return jsonify({"message": "Panier de l'utilisateur non trouvé"}), 404

    cart_item = CartItem.query.filter_by(cart_id=cart.id, product_id=product_id).first()
    if not cart_item:
        return jsonify({"message": "Produit non trouvé dans le panier de l'utilisateur"}), 404

    db.session.delete(cart_item)
    db.session.commit()
    return jsonify({"message": "Produit supprimé du panier avec succès"}), 200

@cart_bp.route('/item-count', methods=['GET'])
@jwt_required()
def get_cart_item_count():
    username = get_jwt_identity()
    current_user = User.query.filter_by(username=username).first()
    
    cart = Cart.query.filter_by(user_id=current_user.id).first()

    if cart is None:
        return jsonify({"count": 0}), 200  

    cart_items_count = db.session.query(func.sum(CartItem.quantity)).filter_by(cart_id=cart.id).scalar()

    return jsonify({"count": cart_items_count}), 200
