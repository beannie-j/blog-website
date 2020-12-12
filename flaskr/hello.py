from flask import Flask, render_template, url_for
app = Flask(__name__)

posts = [
    {
        'author': 'Jeannie An',
        'title': 'Blog Post 1',
        'content': 'First content',
        'date_posted': '12 December 2020'
    },
    {
        'author': 'Jeannie An',
        'title': 'Blog Post 2',
        'content': 'Second content',
        'date_posted': '12 December 2020'
    }
]

@app.route('/')
@app.route('/home')
def hello_world():
    return render_template('home.html', posts=posts, title='Home')

@app.route('/about')
def about():
    return render_template('about.html', title='About')

if __name__ == '__main__':
    app.run(debug=True)