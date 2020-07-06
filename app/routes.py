from flask import render_template, redirect, url_for, request
from flask_login import current_user, login_user, logout_user, login_required
from werkzeug.urls import url_parse
from app import app, db
from app.forms import SignupForm,LoginForm
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
	if current_user.is_authenticated:
		return redirect(url_for('index'))

	form = SignupForm()
	if form.validate_on_submit():
		user = User(username=form.username.data,email=form.email.data)
		user.set_password(form.password.data)
		db.session.add(user)
		db.session.commit()
		# flash a message for successful registration
		return redirect(url_for('login'))


	return render_template('signup.html', title='Ruaraka Friends Church | Signup page', form=form)


@app.route('/login',methods=['GET', 'POST'])
def login():

	if current_user.is_authenticated:
		return redirect('index')

	form = LoginForm()
	if form.validate_on_submit():
		user = User.query.filter_by(email=form.email.data).first()
		if user is None or not user.check_password(form.password.data):
			flash('Invalid User or Password')
			return redirect(url_for('login'))
		login_user(user, remember=form.remember_me.data)
		next_page = request.args.get('next')
		if not next_page or url_parse(next_page).netloc != '':
			next_page = url_for('index')
		return redirect(next_page)
	return render_template('login.html', title='Ruaraka Friends Church | Login', form=form)


@app.route('/logout')
def logout():
	logout_user()
	return redirect(url_for('index'))


@app.route('/profile')
@login_required
def profile():
	user = User.query.filter_by(email=current_user.email).first()
	title = "{} | Profile ".format(user.username)
	return render_template('profile.html',title=title )

