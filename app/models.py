from app import db


class User(db.Model):
	id = db.Column(db.Integer, primary_key=True)
	username = db.Column(db.String(124), index=True,unique=True)
	firstname = db.Column(db.String(124), index=True)
	lastname = db.Column(db.String(124), index=True)
	email = db.Column(db.String(124), index=True, unique=True)
	about_me = db.Column(db.String(150))
	avatar = db.Column(db.String(150))


	def __repr__(self):
		return "<Member : {} >".format(self.username)