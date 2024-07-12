from . import db

class Device(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    ip_address = db.Column(db.String(45), nullable=False)
    status = db.Column(db.String(64), nullable=False)
    last_updated = db.Column(db.DateTime, nullable=False)
