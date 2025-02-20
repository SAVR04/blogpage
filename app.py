from flask import Flask,render_template
from flask_sqlalchemy import SQLAlchemy
from models import db,user
from models import bcrypt


app = Flask(__name__)
app.config["DEBUG"] = True 

# adding configuration for using a sqlite database
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///data.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False 
db.init_app(app)

with app.app_context():
    db.create_all()

#connecting bcrypt to flask
bcrypt.init_app(app)


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