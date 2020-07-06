from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField,SubmitField,BooleanField
from wtforms.validators import ValidationError, DataRequired, Email,Length, EqualTo


from app.models import User

class SignupForm(FlaskForm):
	username = StringField('Username', validators=[DataRequired()])
	email = StringField('Email', validators=[DataRequired(),Email()])
	password = StringField('Password', validators=[DataRequired()])
	password2 = StringField('Confirm Password', validators=[DataRequired(), EqualTo('password')])
	submit = SubmitField('Create account')


	def validate_username(self, username):
		user = User.query.filter_by(username=username.data).first()
		if user is not None:
			raise ValidationError("Use a different username")

	def validate_email(self,email):
		user = User.query.filter_by(email=email.data).first()
		if user is not None:
			raise ValidationError("User a different email address")


class LoginForm(FlaskForm):
	email = StringField('Email', validators=[DataRequired()])
	password = PasswordField('Password', validators=[DataRequired()])
	remember_me = BooleanField('Remember me')
	submit = SubmitField("Sign in")

