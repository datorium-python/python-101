import os
import uuid
import datetime as dt
from flask import Blueprint, render_template, redirect, url_for, flash, current_app, session
from werkzeug.security import generate_password_hash, check_password_hash
from .forms import LoginForm, RegisterForm
from flask_register_app.models.users import User


bp = Blueprint('auth', __name__, url_prefix='/auth')


USERS_DB = {}


@bp.route('/')
def index():
    return redirect(url_for('auth.login'))


@bp.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()

    print(session.items())

    if form.validate_on_submit():
        email = form.email.data
        password = form.password.data

        existing_user = User.get_or_none(User.email == email)
        if not existing_user:
            flash(f'User {email} is not registered!', category='danger')
            return redirect(url_for('auth.login'))

        if not check_password_hash(existing_user.password, password):
            flash(f'User {email} password is not correct!', category='danger')
            return redirect(url_for('auth.login'))

        flash(f'User {email} logged in!', category='success')
        session['is_logged_in'] = True
        session['user_id'] = existing_user.id
        session['user_email'] = existing_user.email
        return redirect(url_for('index'))

    return render_template('login.html', form=form)


@bp.route('/logout')
def logout():
    session.clear()
    return redirect(url_for('auth.login'))


@bp.route('/register', methods=['GET', 'POST'])
def register():
    form = RegisterForm()

    if form.validate_on_submit():
        email = form.email.data

        existing_user = User.get_or_none(User.email == email)
        if existing_user:
            print(existing_user)
            print(existing_user.name)
            print(existing_user.email)
            print(existing_user.password)
            flash(f'User {email} already exists!', category='danger')
            return redirect(url_for('auth.register'))

        password_hash = generate_password_hash(form.password.data)

        filename = ''
        if form.image.data:
            image = form.image.data
            # First simple solution
            # filename = secure_filename(image.filename)

            # Second harder solution
            extension = image.filename.split('.')[1]
            unique_filename = uuid.uuid4()
            filename = f'{unique_filename}.{extension}'

            upload_folder = current_app.config.get('UPLOAD_FOLDER')
            filepath = os.path.join(upload_folder, filename)
            image.save(filepath)

        # Save new user into database
        User.create(
            name=form.full_name.data,
            email=form.email.data,
            image=filename,
            password=password_hash,
            terms=True,
            registered_at=dt.datetime.now()
        )

        flash(f'User {email} registered successfully!', category='success')
        return redirect(url_for('auth.login'))

    return render_template('register.html', form=form)