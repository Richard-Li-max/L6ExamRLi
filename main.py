from flask import Flask, render_template, request, redirect, session
#from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URL'] = 'sqlite:///users.db'
app.secret_key = "password"

#db = SQLAlchemy(app)

#class User(db.Model):
#    id = db.Column(db.Integer, primary_key = True)
#    username = db.Column(db.String(80),unique=True, nullable = False)
#    password = db.Column(db.String(120),unique=True, nullable = False)

#    def __repr__(self):
#        return '<User %r>' % self.username
      
@app.route('/')
@app.route('/login', methods = ['POST', 'GET'])
def login():
    if request.method == "POST":
        #username = request.form.get("username")
        #password = request.form.get("password")

        #user = User.query.filter_by(username = username).first()

        #if user and (password == user.password):
        #    session['username'] = username
        #    return redirect("/")
        #else:
        #    return render_template("login.html", message = "Invalid username or password")
    #else:
        return render_template("login.html")

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
            return render_template("register.html", message = "Passwords do not match!")
        
        #new_user = User(username=username, password=password)

        #db.session.add(new_user)
        #db.session.commit()
            
        return render_template("/index.html")
    else:
        return render_template("/register.html")


if __name__ == '__main__':
    import os
    HOST = os.environ.get('SERVER_HOST', 'localhost')
    try:
        PORT = int(os.environ.get('SERVER_PORT', '5555'))
    except ValueError:
        PORT = 5555
    app.run(HOST, PORT) 