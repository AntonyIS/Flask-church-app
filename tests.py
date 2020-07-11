import unittest
from app import app,db
from app.models import User, Post



class PostModelCase(unittest.TestCase):

	def setUp(self):
		db.create_all()

	def test_app_post(self):
		u = User(username='antony',email='antony@gmail.com')
		u.set_password('pass1234')
		db.session.add(u)
		db.session.commit()
		p1 = Post(title='post by antony', body='test body by antony', user_id=u.id)
		db.session.add(p1)
		db.session.commit()

		self.assertEqual(len(Post.query.all()),1)

	def tearDown(self):
		db.session.remove()
		db.drop_all()

if __name__ == '__main__':
	unittest.main(verbosity=2)

