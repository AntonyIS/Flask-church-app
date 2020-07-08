from flask import render_template, redirect, url_for, request,flash
from flask_login import current_user, login_user, logout_user, login_required
from werkzeug.urls import url_parse
from app import app, db
from app.forms import SignupForm,LoginForm,EditUserProfile,PostForm
from app.models import User, Post

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


@app.route('/profile/<username>', methods=['GET', 'POST'])
def profile(username):
	user = User.query.filter_by(username=username).first()
	posts = None
	owner = False

	try:
		posts = Post.query.filter_by(user_id=user.id)
		if current_user.id == user.id:
			owner = True
	except:
		pass

	title = "{} | Profile ".format(user.username)
	return render_template('profile.html',title=title, user=user,  posts=posts)


@app.route('/profile/edit/<username>', methods=['GET','POST'])
@login_required
def profile_edit(username):
	# check if user is logged in and the requested username is the same as the one for the current_user username
	if current_user.username != username:
		return redirect(url_for('login'))

	form = EditUserProfile(current_user.username)
	if form.validate_on_submit():
		current_user.username = form.username.data
		current_user.firstname = form.firstname.data
		current_user.lastname = form.lastname.data
		current_user.email = form.email.data
		current_user.about_me = form.about_me.data
		current_user.avatar = form.avatar.data
		current_user.role = form.role.data
		db.session.commit()
		flash("Your changes have been submitted")
		return redirect(url_for('profile_edit', username=current_user.username))

	elif request.method == 'GET':
		form.username.data = current_user.username 
		form.firstname.data = current_user.firstname
		form.lastname.data = current_user.lastname
		form.email.data = current_user.email
		form.about_me.data = current_user.about_me
		form.avatar.data = current_user.avatar 
		form.role.data = current_user.role
	title = "{} | Profile ".format(current_user.username)
	return render_template('profile_edit.html',title=title,form=form)



@app.route('/post/add', methods=['GET','POST'])
@login_required
def add_post():
	form = PostForm()
	if form.validate_on_submit():
		post = Post(title=form.title.data, body =form.body.data,user_id=current_user.id)
		db.session.add(post)
		db.session.commit()
		flash('{} added successfully.'.format(form.title.data))
		return redirect(url_for('index'))
	return render_template('post_add.html', title='Add Post', form=form)













@app.route('/members')
def members():
	users = User.query.all()
	return render_template('users.html', title="Ruaraka Friends Church | Edit", users=users)






@app.route('/subscribe', methods=['GET', 'POST'])
def subscribe():
	return render_template('index.html',title="Ruaraka Friends Church | Subscribe" )
