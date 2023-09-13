from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class Product(db.Model):
    __tablename__ = 'product'

    id = db.Column(db.Integer, primary_key=True)
    nom = db.Column(db.String(255))
    prix = db.Column(db.Numeric(10, 2))
    description = db.Column(db.Text)
    image_url = db.Column(db.Text)

    def __init__(self, nom, prix, description, image_url):
        self.nom = nom
        self.prix = prix
        self.description = description
        self.image_url = image_url

class CartItem(db.Model):
    __tablename__ = 'cart_item'

    id = db.Column(db.Integer, primary_key=True)
    cart_id = db.Column(db.Integer, db.ForeignKey('cart.id'))
    product_id = db.Column(db.Integer, db.ForeignKey('product.id'))
    quantity = db.Column(db.Integer, default=1)
    total_price = db.Column(db.Numeric(10, 2))
    product = db.relationship('Product', backref='cart_items')

    def __init__(self, cart_id, product_id, quantity, total_price):
        self.cart_id = cart_id
        self.product_id = product_id
        self.quantity = quantity
        self.total_price = total_price


class Cart(db.Model):
    __tablename__ = 'cart'

    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    items = db.relationship('CartItem', backref='cart', lazy='dynamic')

    def __init__(self, user_id):
        self.user_id = user_id

class User(db.Model):
    __tablename__ = 'user'

    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(255))
    carts = db.relationship('Cart', backref='user', lazy='dynamic')

    def __init__(self, username):
        self.username = username
