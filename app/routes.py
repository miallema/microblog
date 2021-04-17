from flask import render_template
from app import app
from app.forms import LoginForms

@app.route('/')
@app.route('/index')
def index():
	user = {'username': 'Michael'}
	posts = [
		{
			'author': {'username': 'Michael'},
			'body': 'Beautiful day in Lausanne'
		},
		{
			'author': {'username': 'Tania'},
			'body': 'Building buildings'
		}
	]
	return render_template('index.html', title='Home', user=user, posts=posts)

@app.route('/login')
def login():
	form = LoginForm()
	return render_template('login.html', title='Sign In', form=form)
