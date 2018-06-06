from flask import Flask, url_for, request, render_template
app = Flask(__name__)


@app.route('/')
def index():
    """
    index
    """
    return 'Index Page'


@app.route('/hello')
@app.route('/hello/<name>')
def hello(name=None):
    """
    hello world
    """
    return render_template('hello.html', name=name)


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


@app.route('/login', methods=['GET', 'POST'])
def login():
    """
    login
    """
    if request.method == 'POST':
        return about()
    return index()


with app.test_request_context():
    print(url_for('index'))
    print(url_for('login'))
    print(url_for('login', next='/'))
    print(url_for('show_user_profile', username='John Doe'))

with app.test_request_context('/hello', method='POST'):
    # now you can do something with the request until the
    # end of the with block, such as basic assertions:
    assert request.path == '/hello'
    assert request.method == 'POST'
