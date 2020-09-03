from flask import Flask, render_template
from flask_twitter.blueprints.user.models import User
from flask_twitter.blueprints.auth.views import bp


app = Flask(__name__)
app.secret_key = 'qwerty123'
app.debug = True


@app.route('/')
def home():
    return render_template('home.html')


User.create_table()


app.register_blueprint(bp)

# home -> all posts from all users
# user blueprint -> all posts from selected user / ...
# auth blueprint -> login / logout / register
