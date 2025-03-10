from app import db
from datetime import datetime

class Event(db.Model):
    __tablename__ = 'events'

    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(256), nullable=False)
    description = db.Column(db.String(1000), nullable=False)
    date = db.Column(db.DateTime, nullable=False)
    time = db.Column(db.String(10), nullable=False)
    duration = db.Column(db.String(10), nullable=False)
    location = db.Column(db.String(256), nullable=False)
    public = db.Column(db.Boolean, default=True)
    created_at = db.Column(db.DateTime, default=datetime.now().astimezone)
    updated_at = db.Column(db.DateTime, default=datetime.now().astimezone, onupdate=datetime.now().astimezone)
    deleted_at = db.Column(db.DateTime, nullable=True)
