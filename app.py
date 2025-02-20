from flask import Flask, render_template
from models import db, bcrypt  # Import db and bcrypt from models

# Initialize the Flask app
app = Flask(__name__)
app.config["DEBUG"] = True

# Database URI configuration
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///data.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Initialize db with app (this should be in app.py)
db.init_app(app)

# Create database tables
with app.app_context():
    db.create_all()

# Initialize bcrypt with app (this should be in app.py)
bcrypt.init_app(app)

# Define your routes
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
