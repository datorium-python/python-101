from flask import Flask, redirect, url_for
from flask_register_app.blueprints.auth.views import bp


app = Flask(
    __name__,
    static_folder='static',
    template_folder='templates',
)
app.secret_key = 'qwerty'


@app.route('/')
def index():
    return redirect(url_for('auth.login'))


app.register_blueprint(bp)  # Register Blueprint in Flask App
