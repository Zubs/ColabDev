from app.models.user import User
from app import db

class AuthService:
    @staticmethod
    def login(username, password):
        user = User.query.filter_by(username=username, password=password).first()
        if user:
            return user
        return None

    @staticmethod
    def logout():
        return True
