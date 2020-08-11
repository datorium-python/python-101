from flask import Flask, render_template


app = Flask(
    __name__,
    static_folder='static',
    template_folder='templates',
)


@app.route('/', methods=['GET', 'POST'])
def login():
    return render_template('login.html')


@app.route('/register', methods=['GET', 'POST'])
def register():
    return render_template('register.html')


if __name__ == '__main__':
    app.run(
        host='localhost',
        port=8080,
        debug=True
    )