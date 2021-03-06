from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField,SubmitField,BooleanField,TextAreaField, SelectField
from wtforms.validators import ValidationError, DataRequired, Email,Length, EqualTo,Length,Regexp


from app.models import User, Post

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
	role = SelectField(
		'Role',
		choices = [ ('Member','Member'),('Pastor', 'Pastor'),('Praiser','Praiser')]
	)
	# , validators=[Regexp('^(http|https):\/\/[\w.\-]+(\.[\w.\-]+)+.*$', 0, 'URL must be a valid link')]
	facebook_url = StringField('Facebook link')
	twitter_url = StringField('Twitter link')
	linkedin_url = StringField('Linkedin link')
	submit = SubmitField("Update")


	def __init__(self, original_username, *args, **kwargs):
		super(EditUserProfile, self).__init__(*args, **kwargs)
		self.original_username = original_username

	def validate_username(self, username):
		if username.data != self.original_username:
			user = User.query.filter_by(username=self.username.data).first()
			if user is not None:
				raise ValidationError('Please use a different username.')

class PostForm(FlaskForm):
	title = StringField('Title',validators=[DataRequired()])
	body = TextAreaField('Body', validators=[DataRequired(), Length(min=0, max=500)])
	submit = SubmitField('Post')

	# check if similar post exist
	def post_exist(self):
		pass

class PostEditForm(FlaskForm):
	title = StringField('Title',validators=[DataRequired()])
	body = TextAreaField('Post content (Max of 500 words)',validators=[DataRequired()])
	submit = SubmitField("Edit sermon")

class SermonForm(FlaskForm):
	title = StringField('Title',validators=[DataRequired()])
	text = StringField('Bible verse',validators=[DataRequired()])
	body = TextAreaField('Content', validators=[DataRequired(), Length(min=0, max=500)])
	submit = SubmitField("Post a sermon")

class SermonEditForm(FlaskForm):
	title = StringField('Title',validators=[DataRequired()])
	text = StringField('Bible verse',validators=[DataRequired()])
	body = TextAreaField('Content', validators=[DataRequired(), Length(min=0, max=500)])
	submit = SubmitField("Edit sermon")


class ResetPasswordRequestForm(FlaskForm):
	email = StringField('Email', validators=[DataRequired(),Email()])
	submit = SubmitField('Request password reset')


class ResetPasswordForm(FlaskForm):
	password = PasswordField('Password', validators=[DataRequired()])
	password2 = PasswordField('Confirm password', validators=[DataRequired(), EqualTo('password')])
	submit = SubmitField('Request password')
