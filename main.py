from flask import Flask, render_template, request, redirect

app = Flask(__name__)

app.config['DEBUG'] = True


@app.route('/validate', methods=['POST'])
def validate():
    username = request.form['username']
    username_error = ""
    password = request.form['password']
    password_error = ""
    verify = request.form['verify']
    verify_error = ""

    if username == "":
        username_error = "Please enter a valid username."

    if password == "":
        password_error = "Please enter a valid password."

    if verify == "":
        verify_error = "Please correctly re-enter your password."

    return redirect('/?ue=' + username_error + "&pe=" + password_error + "&ve=" + verify_error)

@app.route('/')
def index():
    username_error=request.args.get('ue')
    password_error=request.args.get('pe')
    verify_error=request.args.get('ve')
    return render_template('index.html', username_error=username_error, password_error=password_error, verify_error=verify_error)


app.run()