from flask import Flask, render_template, request
app = Flask(__name__)

@app.route('/')
@app.route('/login', methods = ['post', 'get'])
def login():
    return render_template('login.html')

@app.route("/logout")
def logout():
    return render_template('login.html')


@app.route("/register", methods=['POST', 'GET'])
def regster():
    if request.method == 'POST':
        username = request.form.get('username')
        password = request.form.get('password')
        confirm_password = request.form["confirm-password"]

        if password != confirm_password:
            return render_template("register.html", error = "Passwords do not match!")
            
        return render_template("/index.html")
    else:
        return render_template("register.html")


if __name__ == '__main__':
    import os
    HOST = os.environ.get('SERVER_HOST', 'localhost')
    try:
        PORT = int(os.environ.get('SERVER_PORT', '5555'))
    except ValueError:
        PORT = 5555
    app.run(HOST, PORT) 