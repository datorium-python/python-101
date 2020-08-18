from flask import Blueprint, render_template, redirect, url_for, flash
from werkzeug.security import generate_password_hash, check_password_hash
from .forms import LoginForm, RegisterForm


bp = Blueprint('auth', __name__, url_prefix='/auth')


USERS_DB = {}


@bp.route('/')
def index():
    return redirect(url_for('auth.login'))


@bp.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()

    if form.validate_on_submit():
        email = form.email.data  # email@gmail.com
        password = form.password.data
        if email in USERS_DB:
            user = USERS_DB.get(email)  # {'full_name': '...', 'password': '...'}
            if check_password_hash(user.get('password'), password):
                print('')
                print('### LOGIN INFO ###')
                print(f"User: {user.get('full_name')}")

    print(form.errors)
    return render_template('login.html', form=form)


@bp.route('/register', methods=['GET', 'POST'])
def register():
    form = RegisterForm()

    if form.validate_on_submit():
        # Example: form.email.data
        email = form.email.data
        if email in USERS_DB:
            flash(f'User {email} already exists!', category='danger')
            return redirect(url_for('auth.register'))

        password_hash = generate_password_hash(form.password.data)
        new_user = {
            'full_name': form.full_name.data,
            'password': password_hash,
        }
        USERS_DB[email] = new_user

        flash(f'User {email} registered successfully!', category='success')
        return redirect(url_for('auth.login'))

    print(form.errors)
    return render_template('register.html', form=form)