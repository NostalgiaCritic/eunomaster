from pybo import db

class Contact(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(20), nullable=False)
    number = db.Column(db.String(20), nullable=False)
    create_date = db.Column(db.DateTime(), nullable=False)