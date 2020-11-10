from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class Incidence(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    fk_disease = db.Column(db.Integer, nullable=False)
    date = db.Column(db.DateTime(), nullable=False)