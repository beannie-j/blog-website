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
def get_home_page():
    return render_template('home.html', posts=posts, title='Home')

@app.route('/about')
def get_about_page():
    return render_template('about.html', title='About')

@app.route('/projects')
def get_project_page():
    return render_template('projects.html', posts=posts, title='Projects')

@app.route('/contact')
def get_contact_page():
    return render_template('contact.html', posts=posts, title='Contact')

if __name__ == '__main__':
    app.run(debug=True)