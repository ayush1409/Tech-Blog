from flask import Flask, render_template, url_for
app = Flask(__name__)

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

@app.route('/about')
def about():
	return render_template('about.html', title='About')
