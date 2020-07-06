from flask import render_template, redirect, url_for, request
from flask_login import current_user, login_user, logout_user, login_required
from app import app, db
from app.forms import SignupForm
from app.models import User

# The home route, request to '/' ir '/home' on the browser will be served with this route
@app.route('/')
@app.route('/home')
def index():
	return render_template('index.html', title='Friends Church Ruaraka')



# Authentication routes
# 1.Signup
# 2.Login
# 3.Logout
@app.route('/signup', methods=['GET', 'POST'])
def signup():
	# check if the current user is trying to register
	if current.is_authenticated:
		return redirect(url_for('index'))

	form = SignupForm()
	if form.validate_on_submit():
		user = User(username=form.username.data,email=form.email.data)
		user.set_password()
		db.session.add(user)
		db.session.commit()
		# flash a message for successful registration
		return redirect(url_for('login'))


	return render_template('signup.html', title='Signup page')


@app.route('/login')
def login():
	return "Login here"

@app.route('/logout')
def logout():
	return "Logout here"

