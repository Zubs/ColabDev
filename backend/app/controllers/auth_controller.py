from flask import jsonify, request
from app.services.auth_service import AuthService
from functools import wraps


def token_required(f):
    @wraps(f)
    def decorated(*args, **kwargs):
        token = None

        # Get token from header
        if 'Authorization' in request.headers:
            auth_header = request.headers['Authorization']
            try:
                token = auth_header.split(" ")[1]
            except IndexError:
                return jsonify({'error': 'Token is missing'}), 401

        if not token:
            return jsonify({'error': 'Token is missing'}), 401

        # Verify token
        user, error = AuthService.verify_token(token)
        if error:
            return jsonify({'error': error}), 401

        return f(user, token, *args, **kwargs)

    return decorated


class AuthController:
    @staticmethod
    def login(data):
        if not data or 'username' not in data or 'password' not in data:
            return jsonify({"error": "Invalid data"}), 400

        user, error = AuthService.login(data['username'], data['password'])

        if user:
            return jsonify({
                "message": "Login successful",
                "data": user
            }), 200

        return jsonify({"error": "Invalid username or password"}), 401

    @staticmethod
    @token_required
    def logout(user, token):
        success, error = AuthService.logout(token)

        if success:
            return jsonify({"message": "Logout successful"}), 200

        return jsonify({"error": "No active session"}), 400

    @staticmethod
    @token_required
    def get_profiles(user, token):
        users = AuthService.get_profiles()

        return jsonify([{
            "id": user.id,
            "fullname": user.fullname,
            "username": user.username,
            "email": user.email
        } for user in users])

    @staticmethod
    def register(data):
        if not data or 'fullname' not in data or 'username' not in data or 'email' not in data or 'password' not in data:
            return jsonify({"error": "Invalid data"}), 400

        user, error = AuthService.register(data)

        if user:
            return jsonify({
                "message": "User created successfully",
                "data": user
            }), 201

        return jsonify({"error": error}), 400
