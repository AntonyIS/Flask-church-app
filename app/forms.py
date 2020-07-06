from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField,SubmitField,BooleanField,TextAreaField
from wtforms.validators import ValidationError, DataRequired, Email,Length, EqualTo,Length


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
			raise ValidationError("Use a different email address")


class LoginForm(FlaskForm):
	email = StringField('Email', validators=[DataRequired()])
	password = PasswordField('Password', validators=[DataRequired()])
	remember_me = BooleanField('Remember me')
	submit = SubmitField("Sign in")



class EditUserProfile(FlaskForm):
	username = StringField('Username', validators=[DataRequired()])
	email = StringField('Email', validators=[DataRequired(),Email()])
	firstname = StringField('Firstname')
	lastname = StringField('Lastname')
	about_me = TextAreaField('Bio', validators=[Length(min=0,max=150)])
	avatar = StringField('Profile Picture')
	role = StringField('Role')
	submit = SubmitField("Update")


	def __init__(self, original_username, *args, **kwargs):
		super(EditUserProfile, self).__init__(*args, **kwargs)
		self.original_username = original_username

	def validate_username(self, username):
		if username.data != self.original_username:
			user = User.query.filter_by(username=self.username.data).first()
			if user is not None:
				raise ValidationError('Please use a different username.')

