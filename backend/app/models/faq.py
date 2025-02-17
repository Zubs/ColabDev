from app import db
from datetime import datetime

class FAQ(db.Model):
    __tablename__ = 'faqs'

    id = db.Column(db.Integer, primary_key=True)
    question = db.Column(db.String(500), nullable=False)
    answer = db.Column(db.String(1000), nullable=False)
    public = db.Column(db.Boolean, default=True)
    created_at = db.Column(db.DateTime, default=datetime.astimezone)
    updated_at = db.Column(db.DateTime, default=datetime.astimezone, onupdate=datetime.astimezone)
    deleted_at = db.Column(db.DateTime, nullable=True)
