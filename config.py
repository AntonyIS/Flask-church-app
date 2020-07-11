import os
from dotenv import load_dotenv
import tests

basedir = os.path.abspath(os.path.dirname(__file__))
load_dotenv(os.path.join(basedir,'.flaskenv'))


class Config(object):
	# base config
	SECRET_KEY = os.environ.get('SECRET_KEY') or 'Base-key'
	SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URI') or "sqlite:///" + os.path.join(basedir, 'church.db')
	SQLALCHEMY_TRACK_MODIFICATIONS = False
	TESTING = False
	
	
class DevConfig(Config):
	FLASK_ENV = 'development'
	SECRET_KEY = 'development-key'
	DEBUG = True
	TESTING = True
	print("Development environment")

class ProdConfig(Config):
	FLASK_ENV = 'production'
	SECRET_KEY = 'production-key'
	DEBUG = False
	TESTING = False
	print("Production environment")	


class TestingConfig(Config):
	SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URI') or "sqlite:///" + os.path.join(basedir, 'tests.db')
	FLASK_ENV = 'testing'
	SECRET_KEY = 'testing-key'
	DEBUG = True
	TESTING = True
	tests.PostModelCase()
	
	print("Testing environment")


