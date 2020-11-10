from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class Disease(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(200), unique=True, nullable=False)
    symptoms = db.Column(db.String(1000), nullable=False) 
    