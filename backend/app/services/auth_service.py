from app.models.user import User
from app import db
from datetime import datetime, timedelta
import jwt
from flask import current_app

class AuthService:
    @staticmethod
    def login(username, password):
        try:
            user = User.query.filter_by(username=username).first()

            if user and user.check_password(password):
                # Generate token
                token = AuthService.generate_token(user.id)

                return {
                    'user': user.serialize(),
                    'token': token
                }, None

            return None, "Invalid username or password"
        except Exception as e:
            db.session.rollback()
            return None, str(e)

    @staticmethod
    def logout():
        return True

    @staticmethod
    def generate_token(user_id):
        try:
            payload = {
                'exp': datetime.utcnow() + timedelta(days=1),
                'iat': datetime.utcnow(),
                'sub': user_id
            }
            return jwt.encode(
                payload,
                current_app.config.get('JWT_SECRET_KEY'),
                algorithm='HS256'
            )
        except Exception as e:
            return None

    @staticmethod
    def decode_token(token):
        try:
            payload = jwt.decode(
                token,
                current_app.config.get('JWT_SECRET_KEY'),
                algorithms=['HS256']
            )
            return payload['sub']
        except jwt.ExpiredSignatureError:
            return 'Token expired. Please login again.'
        except jwt.InvalidTokenError:
            return 'Invalid token. Please login again.'

    @staticmethod
    def verify_token(token):
        try:
            user_id = AuthService.decode_token(token)
            if isinstance(user_id, str):
                return None, user_id

            user = User.query.get(user_id)
            if not user:
                return None, "User not found"

            return user, None
        except Exception as e:
            return None, str(e)

    @staticmethod
    def register(data):
        try:
            user = User()
            user.fullname = data['fullname']
            user.username = data['username']
            user.email = data['email']
            user.set_password(data['password'])

            db.session.add(user)
            db.session.commit()

            return user.serialize(), None
        except Exception as e:
            db.session.rollback()
            return None, str(e)
