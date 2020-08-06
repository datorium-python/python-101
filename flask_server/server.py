import random
import hashlib
import datetime as dt
from flask import Flask, request, render_template, abort
from flask_server.forms import BasicForm


app = Flask(
    __name__,
    template_folder='templates'
)
app.secret_key = 'very_secret_key'


@app.route('/')
def home_page():
    return "Welcome to Flask World!"


@app.route('/hello/<name>')
def hello_user(name):
    return f"Hello, {name}!"


@app.route('/hello')
def hello():
    name = request.args.get('name')
    year = request.args.get('year')
    month = request.args.get('month')
    return f"Hello, {name} {year} {month}!"


@app.route('/calculate/<int:a>/<int:b>')  # Route -> Registered URL in Flask
def calculate(a, b):  # View -> Will Run Function when Route if found by Flask
    operator = request.args.get('operator')  # Query Param is not strictly required in View function
    if operator == 'plus':
        result = a + b
    elif operator == 'minus':
        result = a - b
    elif operator == 'multiply':
        result = a * b
    elif operator == 'divide':
        result = a / b
    else:
        result = None

    return f"Result is: {result}"


@app.route('/home')
def home():
    context = {
        'title': 'Home',
        'users': ['Andrew', 'Kate', 'Joe', 'Dan', 'Harry'],
        'random_number': random.randint(1, 10),
        'current_datetime': dt.datetime.now(),
    }
    return render_template('index.html', **context)


@app.route('/about')
def about():
    title = 'About'
    return render_template('about.html', title=title)


@app.route('/contacts')
def contacts():
    title = 'Contacts'
    return render_template('contacts.html', title=title)


@app.route('/req/get')
def req_get():
    print(request)
    return 'Basic GET request'


@app.route('/req/post', methods=['GET', 'POST'])
def req_post():
    return 'Basic POST request'


USERS = []


@app.route('/forms/basic', methods=['GET', 'POST'])
def form_basic():
    form = BasicForm()

    if form.validate_on_submit():
        email = form.email.data
        first_name = form.first_name.data
        last_name = form.last_name.data
        password = form.password.data
        password_hash = hashlib.sha1(password.encode('utf-8')).hexdigest()

        user = {
            'email': email,
            'first_name': first_name,
            'last_name': last_name,
            'password': password_hash,
        }

        USERS.append(user)

    return render_template('forms/basic.html', users=USERS, form=form)


app.run(
    host='localhost',
    port=5000,
    debug=True
)
