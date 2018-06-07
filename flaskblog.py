from flask import Flask, render_template, url_for
from forms import RegistrationForm, LoginForm
app = Flask(__name__)

app.config['SECRET_KEY'] = 'ABCDabcd12344321'

posts = [
	{
		'author' : 'Chris',
		'title' : 'Blog post 1',
		'content' : 'First Post content',
		'date_posted' : 'june 5'

	},
	{
		'author' : 'Bruce',
		'title' : 'Blog post 2',
		'content' : 'Second Post content',
		'date_posted' : 'june 6'
	}
]
@app.route('/')
@app.route('/home')
def hello():
	return render_template('home.html', posts=posts)

@app.route('/register')
def register():
	form = RegistrationForm()
	return render_template('Register.html', title='Register', form=form)

@app.route('/login')
def login():
	form = LoginForm()
	return render_template('Login.html', title='Login', form=form)

@app.route('/about')
def about():
	return render_template('about.html', title='About')
