from flask import Flask, render_template, url_for
app = Flask(__name__)

posts = [
    {
        'author': 'Lior Reytan',
        'title': 'Course Summary 1',
        'content': 'First summary content',
        'date_posted': 'August 27, 2020'
    },
    {
        'author': 'Student94',
        'title': 'Course Summary 2',
        'content': 'Second summary content',
        'date_posted': 'August 28, 2020'
    }
]

@app.route('/')
@app.route('/home')
def home():
    return render_template('home.html', posts=posts)

@app.route('/about')
def about():
    return render_template('about.html', title='About')


if __name__ == '__main__':
	app.run(debug=True)