import os

SECRET_KEY = "b'\x8c$\x9be\xc3:\xfd\x9e\xf1\xa0\x9a\xc7XTeEO\x9d\xa1Y\xf1(\x88\xbe\x9e\xadk0|\xada\xc3'"

basedir = os.path.abspath(os.path.dirname(__file__))

DEBUG = True

SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL', 'postgresql://gven:gven@localhost:5432/produits')

SQLALCHEMY_TRACK_MODIFICATIONS = False


