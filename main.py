from flask import Flask, render_template, request, redirect

app = Flask(__name__)

app.config['DEBUG'] = True


@app.route('/validate', methods=['POST'])
def validate():
    username = request.form['username']
    password = request.form['password']
    verify = request.form['verify']

    username_error = ""
    password_error = ""
    verify_error = ""

    if username == "":
        username_error = "Please enter a valid username."

    if password == "":
        password_error = "Please enter a valid password."

    if verify == "":
        verify_error = "Please correctly re-enter your password."

    return render_template('index.html', username_error=username_error, password_error=password_error, verify_error=verify_error)

@app.route('/')
def index():
    return render_template('index.html')


app.run()