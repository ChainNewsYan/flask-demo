from flask import Flask
app = Flask(__name__)


@app.route('/')
def index():
    """
    index
    """
    return 'Index Page'


@app.route('/hello')
def hello():
    """
    hello world
    """
    return 'Hello, World'


@app.route('/user/<username>')
def show_user_profile(username):
    """
    user profile
    """
    # show the user profile for that user
    return 'User %s' % username


@app.route('/post/<int:post_id>')
def show_post(post_id):
    """
    post
    """
    # show the post with the given id, the id is an integer
    return 'Post %d' % post_id


@app.route('/path/<path:subpath>')
def show_subpath(subpath):
    """
    subpath
    """
    # show the subpath after /path/
    return 'Subpath %s' % subpath


@app.route('/projects/')
def projects():
    """
    projects
    """
    return 'The project page'


@app.route('/about')
def about():
    """
    about page
    """
    return 'The about page'
