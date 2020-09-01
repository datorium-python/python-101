from flask import Flask, render_template


app = Flask(__name__)
app.secret_key = 'qwerty123'
app.debug = True


@app.route('/')
def home():
    return render_template('home.html')


# home -> all posts from all users
# user blueprint -> all posts from selected user / ...
# auth blueprint -> login / logout / register