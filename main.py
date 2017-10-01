from flask import Flask, render_template, request, redirect

app = Flask(__name__)

app.config['DEBUG'] = True


@app.route('/validate', methods=['POST'])
def validate():
    username = request.form['username']
    username_error = ""
    password = request.form['password']
    password_error = ""

    if username == "":
        username_error = "Please enter a valid username."

    if password == "":
        password_error = "Please enter a valid password."

    return redirect('/?ue=' + username_error + "&pe=" + password_error)

@app.route('/')
def index():
    username_error=request.args.get('ue')
    password_error=request.args.get('pe')
    return render_template('index.html', username_error=username_error, password_error=password_error)


app.run()