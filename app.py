from flask import Flask, request, redirect, url_for, flash, render_template, session
from models import db, bcrypt, User  # Import db and bcrypt from models
from models import Blog
from forms import Registerform
# Initialize the Flask app
app = Flask(__name__)
app.config["DEBUG"] = True

# Database URI configuration
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///data.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Secret key config
app.config['SECRET_KEY'] = '95de0a646378b281febadcb6'

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


@app.route("/register", methods=["POST", "GET"])
def register():
    if request.method == 'POST':
        email = request.form['email']
        password = request.form['password']
        password2 = request.form.get('password2', None)  # Use .get() to avoid KeyError

        print(f"Email: {email}, Password: {password}, Confirm Password: {password2}")  # Debugging output

        # Check if passwords match
        if password != password2:
            flash("Passwords do not match!", "danger")
            return redirect(url_for('register'))

        # Check if email is already taken
        existing_user = User.query.filter_by(email=email).first()
        if existing_user:
            flash("Email already registered. Please log in.", "warning")
            return redirect(url_for('login'))

        # Create new user
        new_user = User(email=email)
        new_user.set_password(password)  # Hashing password before saving
        db.session.add(new_user)
        db.session.commit()

        flash("Registration successful! You can now log in.", "success")
        return redirect(url_for('login'))

    return render_template("register.html")


# Login route
@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        # Get form data
        email = request.form.get("email")
        password = request.form.get("password")

        # Look for the user in the database by email
        user = User.query.filter_by(email=email).first()

        # Check if user exists and password matches
        if user and bcrypt.check_password_hash(user.password_hash, password):
            # If login is successful, store user info in the session
            session["user_id"] = user.id  # You can store other details as needed
            flash("Login successful!", "success")
            return redirect(url_for("home"))  # Redirect to home after login
        else:
            flash("Invalid email or password", "danger")  # Flash error message if invalid

    return render_template("login.html")


# Create new blog route - changed to '/write'
@app.route("/write", methods=["GET", "POST"])
def write():
    if "user_id" not in session:
        return redirect(url_for("login"))  # Redirect to login if not logged in

    if request.method == "POST":
        title = request.form.get("title")
        content = request.form.get("content")
        
        # Get the user_id from the session (logged-in user's ID)
        user_id = session["user_id"]

        new_blog = Blog(title=title, content=content, user_id=user_id)  # Include user_id

        db.session.add(new_blog)
        db.session.commit()
        flash("Blog post created successfully!", "success")
        return redirect(url_for("home"))

    return render_template("write.html")



@app.route("/home")
def home():
    if "user_id" not in session:
        return redirect(url_for("login"))  # Redirect to login if not logged in
    blogs = Blog.query.all()
    return render_template("homepage.html", blogs=blogs)


@app.route("/contact")
def contact():
    return render_template("contact.html")


# Logout route
@app.route("/logout")
def logout():
    # Remove user_id from session to log the user out
    session.pop("user_id", None)
    flash("You have been logged out!", "info")
    return redirect(url_for("login"))  # Redirect to login page after logout


if __name__ == "__main__":
    app.run(debug=True)
