import os
from flask import Flask, redirect, url_for
from flask_register_app.blueprints.auth.views import bp


app = Flask(
    __name__,
    static_folder='static',
    template_folder='templates',
)
app.secret_key = 'qwerty'

project_path = os.path.abspath(os.path.dirname(__file__))
upload_folder = os.path.join(project_path, 'uploads')
app.config['UPLOAD_FOLDER'] = upload_folder


@app.route('/')
def index():
    return redirect(url_for('auth.login'))


app.register_blueprint(bp)  # Register Blueprint in Flask App
