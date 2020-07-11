from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_login import LoginManager





app = Flask(__name__)
login = LoginManager(app)
login.login_view = 'login'

db = SQLAlchemy(app)
migrate = Migrate(app, db)

if app.config['ENV'] == 'production':
	app.config.from_object('config.ProdConfig')

elif app.config['ENV'] == 'development':
	app.config.from_object('config.DevConfig')

elif app.config['ENV'] == 'testing':
	app.config.from_object('config.TestingConfig')
	


from app import routes, models, errors