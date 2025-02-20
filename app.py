from flask import Flask,render_template
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
db= SQLAlchemy(app)
app.config["DEBUG"] = True 

class user(db.model):
    name = db.Column(db.string(40),nullable=False)


@app.route("/")
def intro():
    return render_template('intro.html')
   

@app.route("/home")
def home():
    return render_template('homepage.html')

@app.route("/login")
def login():
    return render_template('login.html')

@app.route("/register")
def register():
    return render_template("register.html")

@app.route("/contact")
def contact():
    return render_template("contact.html")

if __name__ == "__main__":
    app.run(debug=True) 