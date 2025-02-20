from flask_sqlalchemy import SQLAlchemy

db= SQLAlchemy(app)
app.config["DEBUG"] = True 

# adding configuration for using a sqlite database
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///data.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False 

class user(db.model):
    name = db.Column(db.string(40),nullable=False)
