from app import db
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import UserMixin
from app import login
from datetime import datetime



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
	facebook_url = db.Column(db.String(200))
	twitter_url = db.Column(db.String(200))
	linkedin_url = db.Column(db.String(200))
	role = db.Column(db.String(124), index=True)
	posts = db.relationship('Post', backref='author', lazy='dynamic')
	sermons = db.relationship('Sermon', backref='author', lazy='dynamic')


	def __repr__(self):
		return "<Member : {} >".format(self.username)


	def set_password(self, password):
		self.password_hash = generate_password_hash(password)

	def check_password(self, password):
		return check_password_hash(self.password_hash,password)




class Post(db.Model):
	id = db.Column(db.Integer, primary_key=True)
	title = db.Column(db.String(124), index=True)
	body = db.Column(db.String(500), index=True)
	avatar = db.Column(db.String(200))
	timestamp = db.Column(db.DateTime, index=True, default = datetime.utcnow)
	user_id = db.Column(db.Integer, db.ForeignKey('user.id'))

	def __repr__(self):
		return self.title

	def set_avatar(self, avater):
		pass

class Sermon(db.Model):
	id = db.Column(db.Integer, primary_key=True)
	title = db.Column(db.String(124), index=True)
	text = db.Column(db.String(124), index=True)
	body = db.Column(db.String(500), index=True)
	created_at = db.Column(db.DateTime, index=True, default = datetime.utcnow)
	user_id = db.Column(db.Integer, db.ForeignKey('user.id'))

	def __repr__(self):
		return "<Sermon : {} >".format(self.title)
