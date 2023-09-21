import unittest
from flask_testing import TestCase
from app import create_app
from models.model import db, Product, User, Cart, CartItem
from flask_jwt_extended import create_access_token


class TestProductService(TestCase):

    def create_app(self):
        app = create_app()
        app.config['TESTING'] = True
        app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///:memory:'
        return app

    def setUp(self):
        db.create_all()
        self.p = {
            'nom': 'Produit 1',
            'prix': 10.99,
            'description': 'Description du produit 1',
            'image_url': 'image1.jpg'}
        u = User(username='admin', admin=1)
        p = Product(self.p['nom'], self.p['prix'],
                    self.p['description'], self.p['image_url'])
        db.session.add_all([u,p])

    def tearDown(self):
        db.session.remove()
        db.drop_all()

    def test_get_products(self):
        access_token = create_access_token(identity='admin')
        response = self.client.get(
            '/produits/', headers={'Authorization': f'Bearer {access_token}'})
        self.assertEqual(response.status_code, 200)
        data = response.get_json()
        self.assertEqual(len(data), 1)

        for elem in self.p.keys():
            self.assertEqual(data[0][elem], self.p[elem])



if __name__ == '__main__':
    unittest.main()
