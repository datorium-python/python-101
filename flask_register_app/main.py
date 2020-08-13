from flask import Flask, render_template
from flask_register_app.forms import LoginForm, RegisterForm
from werkzeug.security import generate_password_hash, check_password_hash


app = Flask(
    __name__,
    static_folder='static',
    template_folder='templates',
)
app.secret_key = 'qwerty'


USERS_DB = {}


@app.route('/', methods=['GET', 'POST'])
@app.route('/login', methods=['GET', 'POST'])
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


@app.route('/register', methods=['GET', 'POST'])
def register():
    form = RegisterForm()

    if form.validate_on_submit():
        # Example: form.email.data
        email = form.email.data
        password_hash = generate_password_hash(form.password.data)
        new_user = {
            'full_name': form.full_name.data,
            'password': password_hash,
        }
        USERS_DB[email] = new_user
        print(USERS_DB)

    print(form.errors)
    return render_template('register.html', form=form)


if __name__ == '__main__':
    app.run(
        host='localhost',
        port=8080,
        debug=True
    )
