import os
#la secret key est utiles pour générer des token. Elle a été générée avec os.urandom(32)
SECRET_KEY = "b'\x8c$\x9be\xc3:\xfd\x9e\xf1\xa0\x9a\xc7XTeEO\x9d\xa1Y\xf1(\x88\xbe\x9e\xadk0|\xada\xc3'"
basedir = os.path.abspath(os.path.dirname(__file__))
DEBUG = True
#adresse de la db pour le dev
# SQLALCHEMY_DATABASE_URI = 'postgresql://gven:gven@localhost:5432/produits'
#utilisation d'une variable d'env pour la prod
SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL') 
SQLALCHEMY_TRACK_MODIFICATIONS = False


