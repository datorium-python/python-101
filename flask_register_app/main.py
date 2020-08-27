import os
from flask import Flask, redirect, url_for, session, render_template, request
from flask_register_app.blueprints.auth.views import bp
from flask_register_app.models.users import User, Comment


app = Flask(
    __name__,
    static_folder='static',
    template_folder='templates',
)
app.secret_key = 'qwerty'

project_path = os.path.abspath(os.path.dirname(__file__))
upload_folder = os.path.join(project_path, 'uploads')
app.config['UPLOAD_FOLDER'] = upload_folder


# To create a table in Peewee
# we need this line
User.create_table()
Comment.create_table()


@app.route('/', methods=['GET', 'POST'])
def index():
    if not session.get('is_logged_in'):
        return redirect(url_for('auth.login'))

    user = User.get_or_none(User.id == session.get('user_id'))
    if request.method == 'POST':
        text = request.form.get('text')

        # Register new comment from user
        Comment.create(
            user=user,
            text=text
        )

    return render_template('index.html', user=user)


app.register_blueprint(bp)  # Register Blueprint in Flask App
