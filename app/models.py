from app import db
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import UserMixin
from app import login




@login.user_loader
def load_user(id):
	return User.query.get(int(id))


class User(UserMixin,db.Model):
	id = db.Column(db.Integer, primary_key=True)
	username = db.Column(db.String(124), index=True,unique=True)
	firstname = db.Column(db.String(124), index=True)
	lastname = db.Column(db.String(124), index=True)
	email = db.Column(db.String(124), index=True, unique=True)
	password_hash = db.Column(db.String(124), index=True, unique=True)
	about_me = db.Column(db.String(150))
	avatar = db.Column(db.String(150))


	def __repr__(self):
		return "<Member : {} >".format(self.username)


	def set_password(self, password):
		self.password_hash = generate_password_hash(password)

	def check_password(self, password):
		return generate_password_hash(self.password_hash,password)