import os
from dotenv import load_dotenv
import tests

basedir = os.path.abspath(os.path.dirname(__file__))
load_dotenv(os.path.join(basedir,'.flaskenv'))


class Config(object):
	# base config
	SECRET_KEY = os.environ.get('SECRET_KEY') or 'this-should-not-be-seen:)'
	SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URI') or "sqlite:///" + os.path.join(basedir, 'church.db')
	SQLALCHEMY_TRACK_MODIFICATIONS = False
	TESTING = False
	POSTS_PER_PAGE = 4
	MAIL_SERVER=os.environ.get('MAIL_SERVER')
	MAIL_PORT = int(os.environ.get('MAIL_PORT') or 25)
	MAIL_USE_TLS = os.environ.get('MAIL_USE_TLS') is not None
	MAIL_USERNAME=os.environ.get('MAIL_USERNAME')
	MAIL_PASSWORD=os.environ.get('MAIL_PASSWORD')
	ADMINS = ['example@example.com']


class DevConfig(Config):
	FLASK_ENV = 'development'
	DEBUG = True
	TESTING = True


class ProdConfig(Config):
	FLASK_ENV = 'production'
	DEBUG = False
	TESTING = False



class TestingConfig(Config):
	SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URI') or "sqlite:///" + os.path.join(basedir, 'tests.db')
	FLASK_ENV = 'testing'
	DEBUG = True
	TESTING = True
