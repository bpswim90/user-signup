from flask import Flask, render_template, request, redirect

app = Flask(__name__)

app.config['DEBUG'] = True


@app.route('/validate', methods=['POST'])
def validate():
    username = request.form['username']
    password = request.form['password']
    verify = request.form['verify']
    email = request.form['email']

    username_error = ""
    password_error = ""
    verify_error = ""
    email_error = ""

    if username == "" or " " in username or len(username) < 3 or len(username) > 20:
        username_error = "Please enter a valid username."
        username = ""

    if password == "" or " " in password or len(password) < 3 or len(password) > 20:
        password_error = "Please enter a valid password."

    if verify == "" or verify != password:
        verify_error = "Please correctly re-enter your password."

    if email == "":
        email_error = ""
    elif email.count("@") != 1 or email.count(".") != 1 or " " in email or len(email) < 3 or len(email) > 20:
        email_error = "Invalid e-mail address."
        email = ""

    if not username_error and not password_error and not verify_error and not email_error:
        return redirect('/welcome?username=' + username)
    else:
        return render_template('index.html', username=username, email=email, username_error=username_error, password_error=password_error, verify_error=verify_error, email_error=email_error)

@app.route('/welcome')
def welcome():
    username = request.args.get('username')
    return render_template('welcome.html', username=username)

@app.route('/')
def index():
    return render_template('index.html')

app.run()