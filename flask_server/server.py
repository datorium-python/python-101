from flask import Flask, request


app = Flask(__name__)


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


app.run(
    host='localhost',
    port=5000,
    debug=True
)
