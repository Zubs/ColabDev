from app.models.user import User
from app.models.token import Token
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
                token, exp_datetime = AuthService.generate_token(user.id)

                if not token:
                    return None, "Unable to login"

                new_token = Token(
                    token=token,
                    user_id=user.id,
                    expires_at=exp_datetime
                )
                db.session.add(new_token)
                db.session.commit()

                return {
                    'user': user.serialize(),
                    'token': token
                }, None

            return None, "Invalid username or password"
        except Exception as e:
            db.session.rollback()
            return None, str(e)

    @staticmethod
    def logout(token):
        try:
            token = Token.query.filter_by(token=token).first()

            if not token:
                return False, "Token not found"

            db.session.delete(token)
            db.session.commit()
            return True, None
        except Exception as e:
            db.session.rollback()
            return False, str(e)

    @staticmethod
    def generate_token(user_id):
        try:
            payload = {
                'exp': datetime.utcnow() + timedelta(days=1),
                'iat': datetime.utcnow(),
                'sub': str(user_id)
            }
            token = jwt.encode(
                payload,
                current_app.config.get('JWT_SECRET_KEY'),
                algorithm='HS256'
            )
            return token, payload['exp']
        except Exception as e:
            return None

    @staticmethod
    def decode_token(token):
        try:
            payload = jwt.decode(
                str(token),
                current_app.config.get('JWT_SECRET_KEY'),
                algorithms=['HS256']
            )
            return int(payload['sub'])
        except jwt.ExpiredSignatureError:
            Token.query.filter_by(token=token).delete()
            db.session.commit()

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

    @staticmethod
    def get_profiles():
        try:
            users = User.query.all()
            return users
        except Exception as e:
            return None
