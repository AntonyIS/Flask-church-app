from flask import render_template, redirect, url_for, request
from app import app


# The home route, request to '/' ir '/home' on the browser will be served with this route
@app.route('/')
@app.route('/home')
def index():
	return "Friends church Ruaraka"



# Authentication routes
# 1.Signup
# 2.Login
# 3.Logout
@app.route('/signup')
def signup():
	return "Signup here"


@app.route('/login')
def login():
	return "Login here"

@app.route('/logout')
def logout():
	return "Logout here"

