from flask import Flask, render_template, url_for
app = Flask(__name__)

posts = [
    {
        'title': 'Pathfinding Visualiser',
        'language': 'C++',
        'library': 'SFML 2D Graphics, ImGui',
        'content': ''
    },

    {
        'title': 'Agario clone',
        'language': 'Python',
        'library': 'Pygame',
        'content': ''
    },

    {
        'title': 'Tetris',
        'language': 'C++',
        'library': 'SFML 2D Graphics, SQLite',
        'content': ''
    }
]

@app.route('/home')
def get_home_page():
    return render_template('home.html', posts=posts, title='Home')

@app.route('/')
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