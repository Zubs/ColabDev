from app import db
from datetime import datetime
from werkzeug.security import generate_password_hash, check_password_hash

class User(db.Model):
    __tablename__ = 'users'

    id = db.Column(db.Integer, primary_key=True)
    fullname = db.Column(db.String(100), nullable=False)
    username = db.Column(db.String(100), nullable=False, unique=True)
    email = db.Column(db.String(100), nullable=False, unique=True)
    password = db.Column(db.String(256), nullable=False)
    created_at = db.Column(db.DateTime, default=datetime.astimezone)
    updated_at = db.Column(db.DateTime, default=datetime.astimezone, onupdate=datetime.astimezone)
    deleted_at = db.Column(db.DateTime, nullable=True)

    def set_password(self, password):
        self.password = generate_password_hash(password, method='pbkdf2:sha256')

    def check_password(self, password):
        return check_password_hash(self.password, password)

    def serialize(self):
        return {
            'id': self.id,
            'fullname': self.fullname,
            'username': self.username,
            'email': self.email,
        }
